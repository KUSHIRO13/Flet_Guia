import flet as ft

def main(page: ft.Page):

    def cambiar_texto(e):
        texto.value = f"El color selecionado es: {casilla.value}"
        page.update()

    casilla = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option('Blue'),
            ft.dropdown.Option('Green'),
            ft.dropdown.Option('Red')
        ]
    )
    confirmar = ft.ElevatedButton('Confirmar', on_click=cambiar_texto)
    texto = ft.Text()
    page.add(casilla, confirmar, texto)
    page.update()

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)