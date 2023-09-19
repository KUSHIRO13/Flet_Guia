import flet as ft

def main(pagina: ft.Page):
    # Evento
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = 'Por Favor ingrese un nombre'
            pagina.update()
        else:
            pagina.clean()
            pagina.add(ft.Text(f'Mucho gusto {txt_name.value}'))
            pagina.update()

    txt_name = ft.TextField(hint_text='Tu nombre', label='Ingresa:')
    pagina.add(txt_name,ft.ElevatedButton('Di tu nombre', on_click=btn_click))

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)