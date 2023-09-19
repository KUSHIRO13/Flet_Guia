import flet as ft


def main(page: ft.Page):
    def boton_clicked(e):
        salida_texto.value = f'La casilla es: {color_dropdown.value}'
        page.update()

    salida_texto = ft.Text()
    submit_btn = ft.ElevatedButton(text='Confirmar', on_click=boton_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option('Red'),
            ft.dropdown.Option('Green'),
            ft.dropdown.Option('Blue'),
        ]
    )
    page.add(color_dropdown,submit_btn,salida_texto)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)