from src.model.usuario_model import Usuario
import flet as ft
class CategoriaView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.route = "/categoria"
        self.bgcolor ="#DFEBE4"
        self.horizontal_alignment ="center"
        
        

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

    
        titulo_cadastrar = ft.Text(value="Cadastrar Categoria",
                        size = 20,
                        font_family="Georgia",
                        weight=ft.FontWeight.BOLD,
                        color="#395F4A",
                        text_align= "center")
        
        self.campo_cadastrar = ft.TextField(label="Nome da Categoria",
                                border_color="#609E7C",
                                border_radius=10,
                                border_width=2.5,
                                margin=10)
        
        botao_salvar = ft.Button(content="Salvar",
                      color="#263F31",
                      bgcolor="#9FC5B0",
                      width=100,
                      )
        
        linha_cadastrar = ft.Row(controls=[self.campo_cadastrar,botao_salvar], width=450) 
        
        container_cadastrar = ft.Container(content=ft.Column(controls=[titulo_cadastrar,
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
                        text_align= "center")

        container_existentes = ft.Container(content=ft.Column(controls=[subtitulo],
                                                              alignment="center",
                                                              horizontal_alignment="center",),
                                                              width=1890,
                                                              height=740,
                                                              border_radius=10,
                                                              bgcolor="#DBE6E0")



        self.controls = [titulo_com_linhas,
                         container_cadastrar,
                         container_existentes]   

