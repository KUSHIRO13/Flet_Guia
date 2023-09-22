import flet as ft

def main(page:ft.Page):

    def registro(e: ft.FilePickerResultEvent):
        print(f'archivo subido {e.files}')

    archivo = ft.FilePicker(on_result=registro)
    page.overlay.append(archivo)
    page.update()
    def subir_archivos(e: ft.FilePickerResultEvent):
        subir_lista = []
        if archivo.result is not None and archivo.result.files is not None:
            for f in archivo.result.files:
                subir_lista.append()



    page.add(ft.ElevatedButton('Subir archivo', on_click=lambda _:archivo.pick_files()))

if __name__ == '__main__':
    ft.app(main)