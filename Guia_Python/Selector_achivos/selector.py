import flet as ft

def main(page: ft.Page):

    def dialogo_resultado(e: ft.FilePickerResultEvent):
        print('Selecionar archivo o directorio: ', e.path)
        print('Selecionar archivo: ', e.files)

    archivo_picker = ft.FilePicker(on_result=dialogo_resultado)
    page.overlay.append(archivo_picker)
    page.update()


    page.add(ft.ElevatedButton('abrir', on_click=lambda _:archivo_picker.pick_files(allow_multiple=True)))

if __name__ == '__main__':
    ft.app(main)