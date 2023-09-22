import flet as ft

def main(page: ft.Page):
    def teclas(e: ft.KeyboardEvent):
        if e.key == 'A' or e.key == 'F':
            comprobacion.value = f'Felicidades si presionastes la {e.key}'
            page.update()
        else:
            comprobacion.value = f'Intentalo de nuevo, presionastes la tecla {e.key}'
            page.update()


    comprobacion = ft.Text()
    page.on_keyboard_event = teclas
    page.add(ft.Text('Presiona la tecla A o F'), comprobacion)

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)