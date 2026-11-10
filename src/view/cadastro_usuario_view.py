from src.model.usuario_model import Usuario
import flet as ft
class CadastroUsuarioView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.route = "/cadastro"
        self.bgcolor ="#DFEBE4"
        self.horizontal_alignment ="center"
        
        self.vertical_alignment = "center"

        titulo = ft.Text(value="Cadastro de Usuário",
                        size = 25,
                        font_family="Georgia",
                        weight=ft.FontWeight.BOLD,
                        color="#395F4A")
        
        titulo = ft.Text(value="Cadastro de Usuário",
                        size = 25,
                        font_family="Georgia",
                        weight=ft.FontWeight.BOLD,
                        color="#395F4A")
        
        self.campo_novo_usuario = ft.TextField(label="Novo Usuário",
                                border_color="#609E7C",
                                border_radius=10,
                                border_width=2.5,
                                margin=10,
                                prefix_icon=ft.Icons.PERSON_OUTLINED)
        
        self.campo_nova_senha = ft.TextField(label="Senha",
                                border_color="#609E7C",
                                border_radius=10,
                                border_width=2.5,
                                password=True,
                                can_reveal_password=True,
                                prefix_icon=ft.Icons.LOCK)
        
        
        botao_cadastrar = ft.Button(content="Cadastre-se",
                      color="#263F31",
                      bgcolor="#9FC5B0",
                      width=210,
                      on_click=self.cadastrar,
                      )
        
        txt_login = ft.Text(value='Já tem uma conta? ')
        
        voltar_login =ft.Button(content=ft.Text('Fazer login',
                                style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, 
                                                   decoration_color="#569170")),
                                color="#47775C",
                                bgcolor='transparent',
                                elevation=0,
                                on_click=self.voltar_login)
        
        linha_login = ft.Row(controls=[txt_login,voltar_login], width=300, alignment=ft.CrossAxisAlignment.CENTER)
        
        container_campo = ft.Container(content=ft.Column(controls=[titulo,
                                                                   self.campo_novo_usuario,
                                                                   self.campo_nova_senha,
                                                                   botao_cadastrar,
                                                                   linha_login], alignment="center",
                                                                   horizontal_alignment="center",),
                                                                   bgcolor="#FCFDFB",
                                                                   width=400,
                                                                   height=450,
                                                                   border_radius=40)

        self.controls = [container_campo]



    def cadastrar(self):
        usuario = self.campo_novo_usuario.value
        senha = self.campo_nova_senha.value
        if usuario == "" or senha == "":
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Peencha todos os campos"), bgcolor="#1A1AB6"))
            return
        resultado = Usuario().cadastrar(usuario,senha)

        if resultado == True:
            #SNAKBAR Mostrando que deu Certo
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Cadastro efeituado com sucesso!"), bgcolor="#21a517"))
        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Erro ao cadastrar. Entre em contato com o adiministrador"), bgcolor="#e0101f"))


    async def voltar_login(self):
        await self.pagina.push_route("/login")
