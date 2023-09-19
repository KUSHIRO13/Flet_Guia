import flet as ft

def main(page: ft.Page):
    def check_cambio(e):
        salida_texto.value = f'Tu aprendistes a saltar?: {toDo_check.value}'
        page.update()

    salida_texto = ft.Text()
    toDo_check = ft.Checkbox(label='ToDO: Para aprender a saltar?', value=False, on_change=check_cambio)
    page.add(toDo_check, salida_texto)

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)