import time

import flet as ft

def main(page: ft.Page):
    texto = ft.Text(value='Hola Mundo', color='red')
    page.controls.append(texto)
    for n in range(10 + 1):
        texto.value = f'Paso {n}'
        page.update()
        time.sleep(2)

    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)