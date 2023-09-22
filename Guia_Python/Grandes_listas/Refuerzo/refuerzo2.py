import flet as ft

def main(page: ft.Page):
    grid = ft.GridView(expand=True, max_extent=150, child_aspect_ratio=1)
    page.add(grid)
    for i in range(5000):
        grid.controls.append(ft.Container(
            ft.Text(value=f'Texto numero {i}'),
            width=100,
            height=100,
            bgcolor=ft.colors.GREEN,
            alignment=ft.alignment.center,
            border_radius=15,
            border=ft.border.all(2,ft.colors.CYAN)
            )
        )

    page.update()

if __name__ == '__main__':
    ft.app(target=main)