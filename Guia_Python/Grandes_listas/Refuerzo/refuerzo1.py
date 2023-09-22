import flet as ft

def main(page: ft.Page):
    lista = ft.ListView(expand=True,spacing=10)
    page.add(lista)

    for l in range(5000):
        lista.controls.append(ft.Text(value=f'Text numero {l}'))
    page.update()

if __name__ == '__main__':
    ft.app(target=main)