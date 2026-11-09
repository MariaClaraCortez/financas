from src.model.usuario_model import Usuario
import flet as ft
class LoginUsuarioView(ft.View):

    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.route = "/login"

        self.bgcolor ="#DFEBE4"
        self.horizontal_alignment ="center"
        
        self.vertical_alignment = "center"

        titulo = ft.Text(value="Tela de login",
                        size = 25,
                        font_family="Georgia",
                        weight=ft.FontWeight.BOLD,
                        color="#395F4A")

        self.controls=[titulo]

        self.campo_usuario = ft.TextField(label="Usuário",
                                        border_color="#609E7C",
                                        border_radius=10,
                                        border_width=2.5,
                                        margin=10)
                
        self.campo_senha = ft.TextField(label="Senha",
                                        border_color="#609E7C",
                                        border_radius=10,
                                        border_width=2.5,
                                        password=True,
                                        can_reveal_password=True)
                
        botao_entrar = ft.Button(content="Entrar",
                              color="#263F31",
                              bgcolor="#9FC5B0",
                              width=210,
                              on_click=self.voltar_cadastro)
                
        ir_cadastrar = ft.Button(content="Cadastrar Novo Usuário",
                              color="#263F31",
                              bgcolor="#9FC5B0",
                              width=210,
                              on_click=self.voltar_cadastro)
        
        self.controls = [titulo, 
                                 self.campo_usuario,
                                 self.campo_senha,
                                 botao_entrar,
                                 ir_cadastrar]
        
        
        
        
        
    async def voltar_cadastro(self):
        await self.pagina.push_route("/cadastro")