import flet as ft

def teclas(page: ft.Page):
    def teclas_presionadas(e: ft.KeyboardEvent):
        page.add(ft.Text(f'Tecla presionada {e.key}'))
        page.update()

    page.on_keyboard_event = teclas_presionadas
    page.add(ft.Text('Presiona Alguna de las teclas que ves'))


ft.app(target=teclas, view=ft.AppView.WEB_BROWSER)