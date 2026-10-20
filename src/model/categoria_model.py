from src.database.conexao import Conexao

class Categoria:
    def __init__(self):
        pass

    @staticmethod
    def adicionar(login:str,tipo:str) -> int:
        conexao,cursor = Conexao().conectar()
        
        if not conexao:
            print("ERRO AO TENTAR ADICIONAR")
            return None
        
        cursor.execute("""
                        INSERT INTO tb_categorias (login,tipo) 
                       VALUES(%s,%s)
                       """,
                       [login,tipo])
        



    @staticmethod
    def recuperar_todos (login:str,tipo:str) -> dict:
        conexao,cursor = Conexao().conectar()

        if not conexao:
            print("ERRO AO TENTAR RECUPERAR")
            return None
        
        cursor.execute("""
                        SELECT login,tipo from tb_categorias
                    """)
 

    @staticmethod
    def excluir (id_categoria:int) -> bool:
        conexao,cursor = Conexao().conectar()

        if not conexao:
            print("ERRO AO EXCLUIR")
            return False
        
        cursor.execute("""

                    """)