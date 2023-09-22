import flet as ft

def main(page: ft.Page):
    lista = ft.ListView(expand=True, spacing=10, item_extent=50)
    page.add(lista)
    for l in range(5100):
        lista.controls.append(ft.Text(f'Texto N°: {l}'))
        if l % 500 == 0:
            page.update()
    page.update()

if __name__ == '__main__':
    ft.app(target=main)