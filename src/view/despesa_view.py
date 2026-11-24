from src.model.despesa_model import Despesa
import flet as ft
class DespesaView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.route = "/despesa"
        self.bgcolor ="#DFEBE4"
        self.horizontal_alignment ="center"

        dados_usuario = pagina.session.store.get("usuario_logado")
        self.nome_usuario = dados_usuario.get("login") 
        

        titulo = ft.Text(value="Despesas do Usuário",
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


        self.lista_despesas=[]

       

        tabela_despesas = ft.DataTable(columns=[ft.DataColumn(label=ft.Text("ID despesa",size=16,weight=ft.FontWeight.BOLD,font_family="Georgia")),
                                                ft.DataColumn(label=ft.Text("Categoria",size=16,weight=ft.FontWeight.BOLD,font_family="Georgia")),
                                                ft.DataColumn(label=ft.Text("Descrição",size=16,weight=ft.FontWeight.BOLD,font_family="Georgia")),
                                                ft.DataColumn(label=ft.Text("Valor",size=16,weight=ft.FontWeight.BOLD,font_family="Georgia")),
                                                ft.DataColumn(label=ft.Text("Data",size=16,weight=ft.FontWeight.BOLD,font_family="Georgia")),
                                                ft.DataColumn(label=ft.Text("Excluir",size=16,weight=ft.FontWeight.BOLD,font_family="Georgia"))],
                                        rows=self.lista_despesas,)

        
        
        self.atualizar_despesas()
        self.controls = [titulo_com_linhas,
                         tabela_despesas,]

    def atualizar_despesas(self):
       todos= Despesa().recuperar_todos(self.nome_usuario)
       self.lista_despesas.clear() 

       for despesas in todos:
            linha= ft.DataRow(cells=[ft.DataCell(ft.Text(str(despesas.get("id_despesa")),text_align="center", size=17)),
                            ft.DataCell(ft.Text(str(despesas.get("tipo")),text_align="center", size=17)),
                            ft.DataCell(ft.Text(str(despesas.get("descricao")),text_align="center", size=17)),
                            ft.DataCell(ft.Text(str(despesas.get("valor")),text_align="center", size=17)),
                            ft.DataCell(ft.Text(str(despesas.get("data")),text_align="center", size=17)),
                            ft.DataCell(ft.FloatingActionButton(icon=ft.Icon(icon=ft.Icons.DELETE_FOREVER_ROUNDED,
                                                                                 color= "#263F31",),
                                                                                 bgcolor="#9FC5B0",
                                                                                 width=45,
                                                                                 height=40,
                                                                                 key = self.id_despesa,
                                                                                 on_click=self.excluir_despesas))]) 
            
            
            self.lista_despesas.append(linha)

       self.pagina.update()

    

    def excluir_despesas (self, e):
        id_despesa = e.control.key
        Despesa().excluir(id_despesa)
        self.atualizar_despesas()

