import flet as ft

def main(page: ft.Page):
    page.add(ft.ElevatedButton('Has click'))
    page.title = 'Ejemplo de Flet'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    txt_numero = ft.TextField(value='0', text_align='right', width=100)
    txt_numero.disabled = True

    def minus_click(e):
        txt_numero.value = str(int(txt_numero.value) - 1)
        page.update()

    def plus_click(e):
        txt_numero.value = str(int(txt_numero.value) + 1)
        page.update()

    page.add(
        ft.Row([
            ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
            txt_numero,
            ft.IconButton(ft.icons.ADD, on_click=plus_click)
        ],
        alignment=ft.MainAxisAlignment.CENTER)
    )
    page.update()


if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)