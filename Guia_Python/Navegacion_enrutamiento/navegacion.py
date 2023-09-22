import flet as ft
from flet import AppBar, ElevatedButton, Page, Text, View, colors

def main(page: Page):
    page.title = 'Navegacion'
    print(f'Ruta inicial {page.route}')

    def cambio_ruta(e):
        print(f'Ruta Cambiada:/{e.route}')
        page.views.clear()
        page.views.append(
            View(
                '/',
                [
                    AppBar(title=Text(value='Menu principal')),
                    ElevatedButton(text='Ir a configuraciones', on_click=lambda _:page.go('/configuracion'))
                ]
            )
        )

        if page.route == '/configuracion':
            # print('Ruta cambiada', page.route)
            page.views.append(
                View(
                    '/configuracion',
                    [
                        AppBar(title=Text('Configuraciones'),bgcolor=colors.SURFACE_VARIANT),
                        Text('Configuraciones', style='bodyMedium')
                    ]
                )
            )
        page.update()

    def eliminar_vistar(e):
        print('Vista Eliminada', e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = cambio_ruta
    page.on_view_pop = eliminar_vistar
    page.go(page.route)

    def configuraciones(e):
        page.go('/configuracion')




if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER)