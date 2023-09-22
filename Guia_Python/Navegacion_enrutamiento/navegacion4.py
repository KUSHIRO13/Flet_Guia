import flet as ft
from flet import AppBar, ElevatedButton, Text, View, colors

def main(page: ft.Page):
    def menu_principal(ruta):
        page.views.clear()
        page.views.append(
            View(
                '/menu-principal',
                [
                    AppBar(title=Text('Menu principal', color=colors.WHITE), bgcolor=colors.CYAN_500, center_title=True),
                    ElevatedButton('Ir al SubMenu', on_click=lambda _:page.go('/sub-menu'))
                ]
            )
        )
        if page.route == '/sub-menu':
            page.views.append(
                View(
                    '/sub-menu',
                    [
                        AppBar(title=Text('Sub Menu', color=colors.WHITE), bgcolor=colors.CYAN_500),
                        Text('Bienvenido al sub menu')
                    ]
                )
            )
        page.update()
    def regresar(vista):
        page.views.pop()
        regresa = page.views[-1]
        page.go(regresa.route)

    page.on_route_change = menu_principal
    page.on_view_pop = regresar
    page.go(page.route)

if __name__ == '__main__':
    ft.app(main, view=ft.WEB_BROWSER, route_url_strategy='hash')