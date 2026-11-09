from src.model.usuario_model import Usuario
import flet as ft
class CadastroUsuarioView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.bgcolor ="#DFEBE4"
        self.horizontal_alignment ="center"
        
        self.vertical_alignment = "center"

        titulo = ft.Text(value="Cadastro de Usuário",
                        size = 25,
                        font_family="Georgia",
                        weight=ft.FontWeight.BOLD,
                        color="#395F4A")
        
        self.campo_novo_usuario = ft.TextField(label="Novo Usuário",
                                border_color="#609E7C",
                                border_radius=10,
                                border_width=2.5,
                                margin=10)
        
        self.campo_nova_senha = ft.TextField(label="Senha",
                                border_color="#609E7C",
                                border_radius=10,
                                border_width=2.5,
                                password=True,
                                can_reveal_password=True)
        
        botao_cadastrar = ft.Button(content="Cadastrar",
                      color="#263F31",
                      bgcolor="#9FC5B0",
                      width=170,
                      on_click=self.cadastrar)
        
        voltar_login = ft.Button(content="Voltar para Login",
                      color="#263F31",
                      bgcolor="#9FC5B0",
                      width=170)

        self.controls = [titulo, 
                         self.campo_novo_usuario,
                         self.campo_nova_senha,
                         botao_cadastrar,
                         voltar_login]



    def cadastrar(self):
        usuario = self.campo_novo_usuario.value
        senha = self.campo_nova_senha.value
        # caso oq estiver no if seje True 
        if Usuario().cadastrar(usuario,senha):
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Cadastro efetuado com sucesso!"), bgcolor="#55DA67"))
        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Erro ao cadastrar. Entre em contato com o adiministrador"), bgcolor="#F72E2E"))