import flet as ft

def main(page: ft.Page):
    for t in range(5001):
        page.controls.append(ft.Text(f'Texto numero: {t}'))
    page.scroll = 'always'
    page.update()

if __name__ == '__main__':
    ft.app(target=main)