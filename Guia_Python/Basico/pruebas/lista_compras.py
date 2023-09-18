# Importamos Flet
import flet as ft

# Funcion principal
def cuerpo(page: ft.Page):
    # Eventos
    def anadir_lista(e):
        page.add(ft.Checkbox(label=casilla.value))
        casilla.value = ''
        casilla.focus()
        casilla.update()

    # Wightes (No se como se escribe)
    casilla = ft.TextField(hint_text='Que vas a anotar en la lista?:')
    boton = ft.ElevatedButton(text='Anotar', on_click=anadir_lista)

    # Agregaciones
    page.add(ft.Row([
        casilla,
        boton
    ]))
    page.update()


if __name__ == '__main__':
    ft.app(target=cuerpo, view=ft.AppView.WEB_BROWSER)