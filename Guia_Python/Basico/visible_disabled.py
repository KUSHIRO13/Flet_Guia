import flet as ft

def main(page: ft.Page):
    primer_nombre = ft.TextField()
    primer_apellido = ft.TextField()
    columna = ft.Column(controls=[
        primer_nombre,
        primer_apellido
    ])
    # primer_nombre.disabled = True
    # primer_apellido.disabled = True
    columna.disabled = True
    # page.add(primer_apellido,primer_apellido)
    page.add(columna)

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)