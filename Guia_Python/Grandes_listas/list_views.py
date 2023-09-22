import flet as ft

def main(page: ft.Page):
    lv = ft.ListView(expand=True,width=500, spacing=10)
    for i in range(5000 + 1):
        lv.controls.append(ft.Text(f'Texto numero: {i}'))
    page.add(lv)
    page.add(ft.ElevatedButton('Boton'),ft.Dropdown(options=[
        ft.dropdown.Option('Escoge la A'),
        ft.dropdown.Option('Escoge la B'),
        ft.dropdown.Option('Escoge la c'),
    ]))
    page.update()

if __name__ == '__main__':
    ft.app(target=main,)