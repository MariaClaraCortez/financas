import flet as ft
class LoginUsuarioView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.route = "/login"
        self.bgcolor ="#DFEBE4"
        self.horizontal_alignment ="center"
        
        self.vertical_alignment = "center"

        titulo = ft.Text(value="Login do Usuário",
                        size = 25,
                        font_family="Georgia",
                        weight=ft.FontWeight.BOLD,
                        color="#395F4A")
        
        self.campo_login_usuario = ft.TextField(label="Novo Usuário",
                                border_color="#609E7C",
                                border_radius=10,
                                border_width=2.5,
                                margin=10)
        
        self.campo_login_senha = ft.TextField(label="Senha",
                                border_color="#609E7C",
                                border_radius=10,
                                border_width=2.5,
                                password=True,
                                can_reveal_password=True)
        
        self.controls=[titulo]