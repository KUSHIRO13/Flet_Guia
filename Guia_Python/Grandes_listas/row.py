import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def main(page: ft.Page):
    r = ft.Row(wrap=True, scroll='always', expand=True)
    page.add(r)
    for i in range(5000):
        r.controls.append(
            ft.Container(
                ft.Text(f'Item {i}'),
                width=100,
                height=100,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.CYAN_50,
                border=ft.border.all(1, ft.colors.CYAN_400),
                border_radius=ft.border_radius.vertical(15,0),
            )
        )
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)