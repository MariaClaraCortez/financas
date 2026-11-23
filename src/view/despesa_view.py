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
        
        self.vertical_alignment = "center"

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
                                                                               bgcolor="#395F4A")])


        lista_despesas=[]



        tabela_despesas = ft.DataTable(columns=[ft.DataColumn(label="Id da Despesa"),
                                                ft.DataColumn(label="Descrição"),
                                                ft.DataColumn(label="Valor"),
                                                ft.DataColumn(label="Categoria"),
                                                ft.DataColumn(label="Data"),],
                                        rows=lista_despesas)
        
        
        self.controls = [titulo_com_linhas]