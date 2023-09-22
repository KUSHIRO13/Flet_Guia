import flet as ft

def main(page: ft.Page):
    # Eventos
    def sacar_pais(e):
        output_text.value = f'Ya veo entonces eres de {casilla1.value}'
        page.update()

    casilla1 = ft.Dropdown(options=[
        ft.dropdown.Option('Colombia'),
        ft.dropdown.Option('Venezuela'),
        ft.dropdown.Option('Ecuador'),
        ft.dropdown.Option('Chile'),
        ft.dropdown.Option('Brazil'),
    ])
    texto = ft.Text('De donde eres?')
    btn_submit = ft.ElevatedButton('Enviar', on_click=sacar_pais)
    output_text = ft.Text()

    # Agregaciones
    page.add(ft.Row([texto]),
             ft.Row([casilla1,btn_submit]),
             output_text)
    page.update()

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)