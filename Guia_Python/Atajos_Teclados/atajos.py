import flet as ft

def main(page: ft.Page):
    def on_keyword(e: ft.KeyboardEvent):
        page.add(
            ft.Text(
                f'Tecla: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}'
            )
        )

    page.on_keyboard_event = on_keyword
    page.add(ft.Text('Presiona alguna tecla, la tecla CTRL, ALT y SHIFT'))

ft.app(target=main, view=ft.AppView.WEB_BROWSER)

