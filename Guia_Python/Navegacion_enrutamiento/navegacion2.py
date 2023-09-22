import flet as ft

def main(page: ft.Page):

    def principal(e: ft.RouteChangeEvent):
        page.add(ft.Text(f'Ruta actual {e.route}'),
                 ft.ElevatedButton('Otra ruta'))

    def principal1(e: ft.RouteChangeEvent):
        page.route = '/principal'
        page.update()

    page.on_route_change = principal
    page.add(ft.ElevatedButton('Cambio de ruta', on_click=principal1))
    page.update()

if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER)