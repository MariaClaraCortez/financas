from src.database.conexao import Conexao

class Usuario:
    def __init__(self):
        pass


    @staticmethod
    def cadastrar(login:str,senha:str) -> bool:

        conexao,cursor = Conexao().conectar()
        try:
            if not conexao:
                print ("ERRO AO TENTAR CONECTAR!")
                return False
            cursor.execute("""
                            INSERT INTO tb_usuarios(login, senha)
                            VALUES (%s,%s)
                            """,
                            [login, senha])
            
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro:
            print(f"ERRO AO INSERIR: {erro}")
            return False


    
    @staticmethod
    def verificar(login:str,senha:str) -> dict:
        conexao,cursor = Conexao().conectar()

        if not conexao:
            print("ERRO AO VERIFICAR")
            return None
        cursor.execute("""
                        SELECT login, senha FROM tb_usuarios
                        WHERE login = %s
                        AND senha = %s
                        """, 
                        [login,senha])
        resutado = cursor.fetchone()
        conexao.close()
        return resutado
