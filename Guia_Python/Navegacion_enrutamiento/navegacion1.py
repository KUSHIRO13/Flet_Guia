import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(f'La ruta es {page.route}'))

    def ruta_cambiada(e: ft.RouteChangeEvent):
        page.add(ft.Text(f'Nueva Ruta: {e.route}'))


    def ir_tienda(e: ft.RouteChangeEvent):
        page.route = '/tienda'
        page.clean()
        page.update()

    page.on_route_change = ruta_cambiada
    page.add(ft.ElevatedButton('Ir a tienda', on_click=ir_tienda))

    page.update()

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)