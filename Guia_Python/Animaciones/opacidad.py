import flet as ft
from flet import Container, ElevatedButton, Row

def main(page: ft.Page):
    contenedor = Container(
        width=150,
        height=150,
        bgcolor='blue',
        border_radius=15,
        animate_opacity=300,
    )

    def cambiar_opacidad(e):
        contenedor.opacity = 0 if contenedor.opacity == 1 else 1
        contenedor.update()

    page.add(contenedor,
             ElevatedButton('Opacidad',on_click=cambiar_opacidad))

if __name__ == '__main__':
    ft.app(main)