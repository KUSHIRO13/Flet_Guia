import flet as ft

def main(page: ft.Page):
    def aceptar_numero(e):
        src = page.get_control(e.src_id)
        src.content.content.value = '0'
        e.control.content.content.value = '1'
        page.update()

    page.add(
        ft.Row([
            ft.Draggable(group='prueba',
                         content=ft.Container(
                             ft.Text(value='1'),
                             height=50,
                             width=50,
                             bgcolor=ft.colors.CYAN_400,
                             alignment=ft.alignment.center,
                             border_radius=15
                         ),
                         content_when_dragging=ft.Container(
                             width=50,
                             height=50,
                             border_radius=15,
                             border=ft.border.all(3,ft.colors.RED_50),
                             bgcolor=ft.colors.GREY
                         ),
                         # content_feedback=ft.Text('Hola')
                         ),
            ft.Container(width=100),
            ft.DragTarget(group='prueba',
                          content=ft.Container(
                              ft.Text(value='0'),
                              height=50,
                              width=50,
                              bgcolor=ft.colors.CYAN_400,
                              alignment=ft.alignment.center,
                              border_radius=15
                          ),on_accept=aceptar_numero),
            ft.DragTarget(group='prueba',
                          content=ft.Container(
                              width=50,
                              height=50,
                              border_radius=15,
                              content=ft.Text(value='2'),
                              bgcolor=ft.colors.ORANGE,
                              alignment=ft.alignment.center
                          ))
        ])
    )

if __name__ == '__main__':
    ft.app(target=main)