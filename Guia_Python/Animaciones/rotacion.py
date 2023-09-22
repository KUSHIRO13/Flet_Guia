import flet as ft
from flet import Container, ElevatedButton
from math import pi

def main(page: ft.Page):

    def rotar(e):
        contenedor.rotate.angle += pi/2
        contenedor.update()

    contenedor = Container(
        width=150,
        height=300,
        bgcolor='orange',
        border_radius=15,
        rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
        animate_rotation=ft.animation.Animation(300, ft.AnimationCurve.BOUNCE_IN_OUT)
    )

    page.add(ft.Row([
        contenedor,

    ],
    alignment=ft.MainAxisAlignment.CENTER),
    ft.Row([
        ElevatedButton('Rotar', on_click=rotar)
    ],
    alignment=ft.MainAxisAlignment.CENTER))

if __name__ == '__main__':
    ft.app(main)