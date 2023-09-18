import flet as ft

def main(page: ft.Page):
    # Eventos
    def evento_boton(e):
        page.add(ft.Text('Distes click'))

    def anadir_clicker(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ''
        new_task.focus()
        new_task.update()

    # Agregaciones
    new_task = ft.TextField(hint_text='Que quieres hacer?', width=300)
    page.add(ft.ElevatedButton(text='Has click', on_click=evento_boton),
             ft.Row([
                 new_task,
                 ft.ElevatedButton('Añadir', on_click=anadir_clicker)
             ]))
    page.update()


ft.app(target=main, view=ft.AppView.WEB_BROWSER)