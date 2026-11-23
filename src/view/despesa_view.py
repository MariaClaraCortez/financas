from src.model.despesa_model import Despesa
import flet as ft
class DespesaView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.route = "/despesa"
        self.bgcolor ="#DFEBE4"
        self.horizontal_alignment ="center"
        
        self.vertical_alignment = "center"

        titulo = ft.Text(value="Despesa do Usuário",
                        size = 35,
                        font_family="Georgia",
                        weight=ft.FontWeight.BOLD,
                        color="#395F4A",
                        text_align="center")
        
        
        
        self.controls = [titulo]