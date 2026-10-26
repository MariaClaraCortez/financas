from src.database.conexao import Conexao

class Categoria:
    def __init__(self):
        pass

    @staticmethod
    def adicionar(login:str,tipo:str) -> int:
        conexao,cursor = Conexao().conectar()
        
        if not conexao:
            print("ERRO AO TENTAR CONECTAR")
            return None
        
        try:
            cursor.execute("""
                            INSERT INTO tb_categorias (login,tipo) 
                        VALUES(%s,%s)
                        """,
                        [login,tipo])
            id_categoria = cursor.lastrowid
            conexao.commit()
            conexao.close()
            return id_categoria
        except Exception as erro:
            print(f"ERRO AO INSERIR: {erro}")
            return False

        
        



    @staticmethod
    def recuperar_todos (login:str,tipo:str) -> dict:
        conexao,cursor = Conexao().conectar()

        if not conexao:
            print("ERRO AO TENTAR CONECTAR")
            return None
        
        cursor.execute("""
                        SELECT login,tipo from tb_categorias
                    """)
        
        dados = cursor.fetchall()
        
        return dados
 

    @staticmethod
    def excluir (id_categoria:int) -> bool:
        conexao,cursor = Conexao().conectar()

        if not conexao:
            print("ERRO AO CONECTAR")
            return False
        
        cursor.execute("""

                    """)