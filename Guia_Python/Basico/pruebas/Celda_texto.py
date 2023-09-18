import time

import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Row([
            ft.Text('Hola como estas?')
        ]),
        ft.Row([
            ft.Text('Como te llamas?: '),
            ft.TextField(label='Ingrese su nombre'),
            ft.ElevatedButton('Enviar')
        ])
    )
    for i in range(10 + 1):
        page.add(ft.Text(f'Texto {i}'))
        if i > 4:
            page.controls.pop(0)
    page.update()
    time.sleep(0.3)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)