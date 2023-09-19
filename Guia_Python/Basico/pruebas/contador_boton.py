import flet as ft

def principal(page: ft.Page):
    page.title = 'Contador'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    txt_numero = ft.TextField(value='0', text_align='center', width=100)
    txt_numero.disabled = True
    def evento_subir(e):
        txt_numero.value = str(int(txt_numero.value) + 1)
        page.update()

    def evento_bajar(e):
        txt_numero.value = str(int(txt_numero.value) - 1)
        page.update()

    page.add(ft.Row([
        ft.IconButton(ft.icons.REMOVE, on_click=evento_bajar),
        txt_numero,
        ft.IconButton(ft.icons.ADD, on_click=evento_subir)
    ],
    alignment=ft.MainAxisAlignment.CENTER))

if __name__ == '__main__':
    ft.app(target=principal, view=ft.AppView.WEB_BROWSER)