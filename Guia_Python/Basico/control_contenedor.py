import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Row(controls=[
            ft.Text('A'),
            ft.Text('B'),
            ft.Text('C')
        ]),
        ft.Row(controls=[
            ft.TextField(label='Tu Nombre'),
            ft.ElevatedButton(text='Di mi nombre!')
        ])
    )
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)