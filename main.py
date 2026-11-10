import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import LoginUsuarioView
from src.view.principal_usuario_view import PrincipalUsuarioView
from src.view.add_despesa_view import AddDespesaView
from src.view.despesa_categoria_view import DespesaPorCategoriaView
from src.view.despesa_view import DespesaView
from src.view.categoria_view import CategoriaView

def main(pagina:ft.Page):
    
    # e = componente
    def navegacao(e):
        item_clicado = e.control.selected_index
        if item_clicado == 0:
            pagina.navigate("/principal")
        elif item_clicado == 1:
            pagina.navigate("/categoria")
        elif item_clicado == 2:
            pagina.navigate("/add_despesa")
        elif item_clicado == 3:
            pagina.navigate("/despesa")
        elif item_clicado == 4:
            pagina.navigate("/despesa_categoria")
        elif item_clicado == 5:
            pagina.navigate("/login")
        

    barra_vagegacao = ft.NavigationBar(destinations=[
                                        ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Principal"),
                                        ft.NavigationBarDestination(icon=ft.Icons.CATEGORY, label="Caregoria"),
                                        ft.NavigationBarDestination(icon=ft.Icons.ADD_SHOPPING_CART, label="Adicionar Despesa"),
                                        ft.NavigationBarDestination(icon=ft.Icons.ATTACH_MONEY_OUTLINED, label="Despesa"),
                                        ft.NavigationBarDestination(icon=ft.Icons.FEED_OUTLINED, label="Despesa por Categoria"),
                                        ft.NavigationBarDestination(icon=ft.CupertinoIcons.SQUARE_ARROW_RIGHT, label="Sair"),
                                        ],
                                        on_change=navegacao)



   
    
    
    
    
    
    
    
    
    
    
    

    def roteamento(e=None):
        pagina.views.clear()

        if pagina.route == "/cadastro":
            tela_cadastro_usuario = CadastroUsuarioView(pagina)
            pagina.views.append(tela_cadastro_usuario)

        elif pagina.route == "/login":
            tela_login_usuario = LoginUsuarioView(pagina)
            pagina.views.append(tela_login_usuario)

        elif pagina.route == "/principal":
            tela_principal_usuario = PrincipalUsuarioView(pagina)
            tela_principal_usuario.navigation_bar = barra_vagegacao
            pagina.views.append(tela_principal_usuario)
        
        elif pagina.route == "/add_despesa":
            tela_add_despesa = AddDespesaView(pagina)
            tela_add_despesa.navigation_bar = barra_vagegacao
            pagina.views.append(tela_add_despesa)

        elif pagina.route == "/despesa":
            tela_despesa = DespesaView(pagina)
            tela_despesa.navigation_bar = barra_vagegacao
            pagina.views.append(tela_despesa)

        elif pagina.route == "/despesa_categoria":
            tela_despesa_categoria = DespesaPorCategoriaView(pagina)
            tela_despesa_categoria.navigation_bar = barra_vagegacao
            pagina.views.append(tela_despesa_categoria)

        elif pagina.route == "/categoria":
            tela_categoria = CategoriaView(pagina)
            tela_categoria.navigation_bar = barra_vagegacao
            pagina.views.append(tela_categoria)
 

        pagina.update()

    # quando a pagina mudar de rota
    pagina.on_route_change = roteamento
    roteamento()
    pagina.navigate("/login")

ft.run(main)