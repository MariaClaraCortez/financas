import flet as ft
class PrincipalUsuarioView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.route = "/principal"
        dados_usuario = pagina.session.store.get("usuario_logado")
        nome_usuario = dados_usuario.get("login") 
        self.bgcolor ="#DFEBE4"
        self.horizontal_alignment ="center"
        
        self.vertical_alignment = "center"

        titulo = ft.Text(value=f"Seja Bem Vindo {nome_usuario}!",
                        size = 25,
                        font_family="Georgia",
                        weight=ft.FontWeight.BOLD,
                        color="#395F4A")
        

        texto_explicativo = ft.Text(value="""O aplicativo de Controle de Despesas Pessoais foi criado para ajudar as pessoas a administrar melhor seu dinheiro de forma simples e organizada.
Ao acessar o sistema, o usuário encontra um menu principal com diferentes funcionalidades. Na opção Categoria, é possível organizar os tipos de gastos. Em Adicionar Despesa, o usuário pode registrar novos gastos, mantendo suas informações financeiras atualizadas.
Na seção Despesa, é possível consultar as despesas cadastradas. Já em Despesa por Categoria, os gastos são organizados de acordo com suas classificações, facilitando a identificação de onde o dinheiro está sendo utilizado.
O aplicativo reúne essas ferramentas em um único lugar, tornando o acompanhamento financeiro mais prático e ajudando o usuário a desenvolver hábitos de consumo mais conscientes.""")
        
        self.controls =[titulo,
                        texto_explicativo]

    