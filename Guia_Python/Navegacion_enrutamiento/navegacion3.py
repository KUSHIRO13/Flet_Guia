import flet as ft

def main(page: ft.Page):
    page.title = 'Ejemplos rutas'

    def cambio_rutas(ruta):
        print(f'Ruta actual {page.route}')
        page.views.clear()
        page.views.append(
            ft.View(
                '/principal',
                [
                    ft.AppBar(title=ft.Text('Archivo de aplicacion'), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton('Visita de tienda', on_click=lambda _:page.go('/tienda'))
                ]
            )
        )
        if page.route == '/tienda':
            page.views.append(
                ft.View(
                    '/tienda',
                    [
                        ft.AppBar(title=ft.Text('Tienda'),  bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton('Regresar', on_click=lambda _:page.go('/principal'))
                    ]
                )
            )

        page.update()

    def eliminar_vista(vista):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)



    page.on_route_change = cambio_rutas
    page.on_view_pop = eliminar_vista
    page.go(page.route)
    page.update()

if __name__ == '__main__':
    ft.app(main, view=ft.WEB_BROWSER)