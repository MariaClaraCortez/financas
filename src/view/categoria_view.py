from src.model.usuario_model import Usuario
from src.model.categoria_model import Categoria
import flet as ft
class CategoriaView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.route = "/categoria"
        self.bgcolor ="#DFEBE4"
        self.horizontal_alignment ="center"
        

        dados_usuario = pagina.session.store.get("usuario_logado")
        self.nome_usuario = dados_usuario.get("login") 
        

        titulo = ft.Text(value="Categoria",
                        size = 35,
                        font_family="Georgia",
                        weight=ft.FontWeight.BOLD,
                        color="#395F4A",
                        text_align= "center",
                        )

        titulo_com_linhas = ft.Row(alignment="center",
                                   vertical_alignment="center", 
                                   controls=[ft.Container(expand=True,
                                                          height=0.5,
                                                          bgcolor="#395F4A"),
                                                          ft.Container(content=titulo),
                                                          ft.Container(expand=True,
                                                                       height=0.5,
                                                                       bgcolor="#395F4A")])

        
        self.campo_cadastrar = ft.TextField(label="Nome da Categoria",
                                border_color="#609E7C",
                                border_radius=10,
                                border_width=2.5,
                                margin=10)
        
        botao_salvar = ft.Button(content="Salvar",
                      color="#263F31",
                      bgcolor="#9FC5B0",
                      width=100,
                      on_click=self.cadastra_categoria)
        
        linha_cadastrar = ft.Row(controls=[self.campo_cadastrar,botao_salvar], width=450) 
        
        container_cadastrar = ft.Container(content=ft.Column(controls=[titulo_com_linhas,
                                                                   linha_cadastrar],
                                                                        alignment="center",
                                                                        horizontal_alignment="center",),
                                                                        width=5000,
                                                                        border_radius=10)
        
        subtitulo = ft.Text(value="Categoria Existentes",
                        size = 20,
                        font_family="Georgia",
                        weight=ft.FontWeight.BOLD,
                        color="#395F4A",
                        text_align="center",
                        margin=10)

        self.lista_categorias=[]

        container_existentes = ft.Container(content=ft.Column(controls=[subtitulo,
                                                            ft.Column(controls= self.lista_categorias)],
                                                                      alignment="top", horizontal_alignment="center"),
                                                              width=1890,
                                                              height=740,
                                                              border_radius=10,
                                                              bgcolor="#DBE6E0")



        self.atualizar_lista()

        self.controls = [container_cadastrar,
                         container_existentes]


    def cadastra_categoria(self):
        nome_categoria = self.campo_cadastrar.value
        resultado = Categoria().adicionar(self.nome_usuario,nome_categoria)


        if resultado:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Cadastro efetuado com sucesso!"), bgcolor="#21a517"))
        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("ERRO AO CADASTRAR"), bgcolor="#e0101f"))

        self.atualizar_lista()

    def atualizar_lista(self):
        categorias = Categoria().recuperar_todos(self.nome_usuario)
        self.lista_categorias.clear() 

        for categoria in categorias:
            nome_categoria =categoria.get("tipo")
            id_categoria = categoria.get("id_categoria") 

            botao_excluir = ft.FloatingActionButton(icon=ft.Icon(icon=ft.Icons.DELETE_FOREVER_ROUNDED,
                                                                 color= "#263F31",),
                                                                 bgcolor="#9FC5B0",
                                                                 width=45,
                                                                 height=40,
                                                                 on_click=self.excluir,
                                                                 key=id_categoria)
            
            campo_tipo = ft.TextField(value=nome_categoria,
                                      border_color="#518367",
                                      border_radius=10,
                                      border_width=2.5,
                                      margin=3,
                                      read_only=True,
                                      text_align="center")
            
            linha_campinhos= ft.Row(controls=[campo_tipo,botao_excluir], alignment=ft.MainAxisAlignment.CENTER)

            self.lista_categorias.append(linha_campinhos)
        self.pagina.update()

    def excluir(self,e):
        id_categoria = e.control.key
        Categoria().excluir(id_categoria)
        self.atualizar_lista()

