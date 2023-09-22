import flet as ft

def main(page: ft.Page):
    page.title = "Ejemplo de arrastrar y soltar"

    # Evento
    def aceptar_obj(e):
        src = page.get_control(e.src_id)
        src.content.content.value = '0'
        e.control.content.content.value = '1'
        page.update()


    # Agregaciones
    page.add(
        ft.Row([
            ft.Draggable(group='numero',content=ft.Container(width=50,height=50,bgcolor=ft.colors.TEAL,border_radius=5,content=ft.Text('1', size=20),alignment=ft.alignment.center)),
            ft.Container(width=100),
            ft.DragTarget(group='numero',content=ft.Container(width=50,height=50,bgcolor=ft.colors.GREEN_200,border_radius=5,content=ft.Text('0', size=20),alignment=ft.alignment.center),on_accept=aceptar_obj)

        ])
    )

ft.app(target=main)