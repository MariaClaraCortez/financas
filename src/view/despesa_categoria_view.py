from src.model.despesa_model import Despesa
from src.model.categoria_model import Categoria
import flet as ft
class DespesaPorCategoriaView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.route = "/despesa_categoria"
        self.bgcolor ="#DFEBE4"
        self.horizontal_alignment ="center"
        
        

        dados_usuario = pagina.session.store.get("usuario_logado")
        self.nome_usuario = dados_usuario.get("login") 
        

        titulo = ft.Text(value="Despesas por Categoria do Usuário",
                        size = 35,
                        font_family="Georgia",
                        weight=ft.FontWeight.BOLD,
                        color="#395F4A",
                        text_align="center")

        titulo_com_linhas = ft.Row(alignment="center",
                                           vertical_alignment="center", 
                                           controls=[ft.Container(expand=True,
                                                                  height=0.5,
                                                                  bgcolor="#395F4A"),
                                                                  ft.Container(content=titulo),
                                                                  ft.Container(expand=True,
                                                                               height=0.5,
                                                                               bgcolor="#395F4A")],
                                                                               margin=ft.Margin.only(bottom=20))
        
        opcoes_categoria = []

        categorias = Categoria().recuperar_todos(self.nome_usuario)

        for categoria in categorias:
            opcao=ft.DropdownOption(key=categoria.get("id_categoria"), 
                              text=categoria.get("tipo"))
            opcoes_categoria.append(opcao)

        self.campo_categoria = ft.Dropdown(options=opcoes_categoria,
                                           on_select=self.atualizar_despesas,
                                           label="Categoria",
                                           border_color="#609E7C",
                                           border_radius=10,
                                           border_width=2.5,
                                           margin=10,
                                           width=450,)


        self.lista_despesas=[]

       

        tabela_despesas = ft.DataTable(columns=[ft.DataColumn(label=ft.Text("ID despesa",size=16,weight=ft.FontWeight.BOLD,font_family="Georgia")),
                                                ft.DataColumn(label=ft.Text("Descrição",size=16,weight=ft.FontWeight.BOLD,font_family="Georgia")),
                                                ft.DataColumn(label=ft.Text("Valor",size=16,weight=ft.FontWeight.BOLD,font_family="Georgia")),
                                                ft.DataColumn(label=ft.Text("Data",size=16,weight=ft.FontWeight.BOLD,font_family="Georgia")),
                                                ft.DataColumn(label=ft.Text("Excluir",size=16,weight=ft.FontWeight.BOLD,font_family="Georgia"))],
                                        rows=self.lista_despesas,)

        
        
        self.atualizar_despesas()
        self.controls = [titulo_com_linhas,
                         self.campo_categoria,
                         tabela_despesas,]

    def atualizar_despesas(self):
       id_categoria = self.campo_categoria.value
       todos= Despesa().recuperar_por_categoria(self.nome_usuario,id_categoria)
       self.lista_despesas.clear() 

       for despesas in todos:
            id_despesa= str(despesas.get("id_despesa"))
            linha= ft.DataRow(cells=[ft.DataCell(id_despesa),
                            ft.DataCell(ft.Text(str(despesas.get("descricao")),text_align="center", size=17)),
                            ft.DataCell(ft.Text(str(despesas.get("valor")),text_align="center", size=17)),
                            ft.DataCell(ft.Text(str(despesas.get("data")),text_align="center", size=17)),
                            ft.DataCell(ft.FloatingActionButton(icon=ft.Icon(icon=ft.Icons.DELETE_FOREVER_ROUNDED,
                                                                                 color= "#263F31",),
                                                                                 bgcolor="#9FC5B0",
                                                                                 width=45,
                                                                                 height=40,
                                                                                 key =id_despesa,
                                                                                 on_click=self.excluir_despesas))]) 
            
            
            self.lista_despesas.append(linha)

       self.pagina.update()

    

    def excluir_despesas (self, e):
        id_despesa = e.control.key
        Despesa().excluir(id_despesa)
        self.atualizar_despesas()
