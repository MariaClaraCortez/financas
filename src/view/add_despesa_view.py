from src.model.usuario_model import Usuario
from src.model.categoria_model import Categoria
from src.model.despesa_model import Despesa
from datetime import datetime

import flet as ft
class AddDespesaView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.route = "/add_despesa"
        self.bgcolor ="#DFEBE4" 
        self.horizontal_alignment = "center"

        dados_usuario = pagina.session.store.get("usuario_logado")
        self.nome_usuario = dados_usuario.get("login") 
                
        
        titulo = ft.Text(value="Despesa",
                        size = 35,
                        font_family="Georgia",
                        weight=ft.FontWeight.BOLD,
                        color="#395F4A",
                        text_align="center",
                        )

        titulo_com_linhas = ft.Row(alignment="center",
                                           vertical_alignment="center", 
                                           controls=[ft.Container(expand=True,
                                                                  height=0.5,
                                                                  bgcolor="#395F4A",),
                                                                  ft.Container(content=titulo),
                                                                  ft.Container(expand=True,
                                                                               height=0.5,
                                                                               bgcolor="#395F4A",),],
                                                                               margin=ft.Margin.only(bottom=50))


        self.campo_descricao=ft.TextField(label="Descrição",
                                border_color="#609E7C",
                                border_radius=10,
                                border_width=2.5,
                                margin=10,
                                width=450)

        self.campo_valor = ft.TextField(label="Valor",
                                border_color="#609E7C",
                                border_radius=10,
                                border_width=2.5,
                                margin=10,
                                width=450)

        self.campo_data = ft.TextField(label="Data",
                                border_color="#609E7C",
                                border_radius=10,
                                border_width=2.5,
                                margin=10,
                                width=450)

        opcoes_categoria=[]
        categorias = Categoria().recuperar_todos(self.nome_usuario)

        for categoria in categorias:
            opcao=ft.DropdownOption(key=categoria.get("id_categoria"), 
                              text=categoria.get("tipo"))
            opcoes_categoria.append(opcao)


        self.campo_categoria= ft.Dropdown(label="Categoria",
                                border_color="#609E7C",
                                border_radius=10,
                                border_width=2.5,
                                margin=10,
                                width=450,
                                options=opcoes_categoria)

        botao_adicionar = ft.Button(content="Adicionar",
                              color="#263F31",
                              bgcolor="#9FC5B0",
                              width=225,
                              on_click=self.add)
        
        self.controls = [titulo_com_linhas,
                         self.campo_descricao,
                         self.campo_valor,
                         self.campo_data,
                         self.campo_categoria,
                         botao_adicionar]


    def add(self):
        descricao= self.campo_descricao.value
        valor = self.campo_valor.value
        data = self.campo_data.value
        id_categoria = self.campo_categoria.value

        data_convertida = datetime.strptime(data, "%d/%m/%Y").date()

        resultado = Despesa().incluir(self.nome_usuario,id_categoria,descricao,valor,data_convertida)
        if descricao == "" or valor == "" or data == "" or id_categoria == "":
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Peencha todos os campos"), bgcolor="#1A1AB6"))
            return
        
        if resultado:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Despesa adicionada com sucesso!"), bgcolor="#21a517"))
            
        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("ERRO AO ADICIONAR"), bgcolor="#e0101f"))
            
        self.campo_descricao.value=""
        self.campo_categoria.value=""
        self.campo_valor.value = ""
        self.campo_data.value = ""
        self.pagina.update()
    