import flet as ft
class CadastroUsuarioView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()

        titulo = ft.Text(value="Cadastro de Usuário")

        pagina.controls = [titulo]
