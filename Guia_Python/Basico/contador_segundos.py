import time

import flet as ft

def main(page: ft.Page):
    texto = ft.Text(value='Hola, que tal')
    page.add(texto)
    time.sleep(5)
    texto2 = ft.Text(value='')
    page.add(texto2)
    # Creacion del contador
    for n in range(10 + 1):
        texto2.value = f'Paso: {n} segundos'
        page.update()
        time.sleep(1)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)