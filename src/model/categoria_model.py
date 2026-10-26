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
    def recuperar_todos (login:str) -> list[dict]:
        conexao,cursor = Conexao().conectar()

        if not conexao:
            print("ERRO AO TENTAR CONECTAR")
            return None
        
        try:
            cursor.execute("""
                            SELECT login,tipo from tb_categorias
                           WHERE login = %s
                        """,[login])
            
            dados = cursor.fetchall()
            conexao.close()
            return dados
        except Exception as erro:
            print(f"ERRO AO INSERIR: {erro}")
            return False
        
        
 

    @staticmethod
    def excluir (id_categoria:int) -> bool:
        conexao,cursor = Conexao().conectar()

        if not conexao:
            print("ERRO AO CONECTAR")
            return False
        try:
            cursor.execute("""
                            DELETE FROM tb_categorias WHERE id_categoria = %s
                        """,[id_categoria])
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro:
            print(f"ERRO AO EXCLUIR: {erro}")
            return False
