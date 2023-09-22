import flet as ft

def main(page: ft.Page):
    # Formas de aplicar color
    c1 = ft.Container(ft.TextField(border_radius=15),bgcolor='#ff0000')
    c2 = ft.Container(ft.TextField(),bgcolor=ft.colors.BLUE)
    c3 = ft.Container(ft.TextField(),bgcolor='yellow')
    c4 = ft.Container(ft.TextField(),bgcolor=ft.colors.GREEN_200)
    page.add(c1, c2, c3, c4)
    # Valor por incremento
    color_50 = ft.Container(ft.TextField(), bgcolor=ft.colors.BLUE_50)
    color_100 = ft.Container(ft.TextField(), bgcolor=ft.colors.BLUE_100)
    color_200 = ft.Container(ft.TextField(), bgcolor=ft.colors.BLUE_200)
    color_300 = ft.Container(ft.TextField(), bgcolor=ft.colors.BLUE_300)
    page.add(color_50,color_100,color_200,color_300)
    # Valor de opacidad
    page.add(ft.Container(ft.TextField(), bgcolor='orange52'))
    # Con opacidad
    # color1 = ft.colors.with_opacity(0.2, ft.colors.PRIMARY)
    # color2 = ft.colors.with_opacity(0.9, '#FF1233')
    # page.add(ft.Container(ft.TextField(), bgcolor=color2))
    container = ft.Container(
        width=200,
        height=200,
        border=ft.border.all(1, ft.colors.BLACK),
        content=ft.FilledButton("Primary color"),
        theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.YELLOW)))

    page.add(container)


    page.update()

if __name__ == '__main__':
    ft.app(target=main)
    # , view=ft.AppView.WEB_BROWSER