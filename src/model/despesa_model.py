from src.database.conexao import Conexao

class Despesa:
    def __init__(self):
        pass

    @staticmethod
    def incluir(login:str,id_categoria:int,descricao:str,valor:float,data:str,hora:str) -> int:
        conexao,cursor = Conexao().conectar()
        
        if not conexao:
            print("ERRO AO TENTAR CONECTAR")
            return None
        
        try:
            cursor.execute("""
                            INSERT INTO tb_despesa (login,id_categoria,descricao,valor,data,hora) 
                        VALUES(%s,%s,%s,%s,%s,%s)
                        """,
                        [login,id_categoria,descricao,valor,data,hora])
            id = cursor.lastrowid
            conexao.commit()
            conexao.close()
            return id
        except Exception as erro:
            print(f"ERRO AO INSERIR: {erro}")
            return False
