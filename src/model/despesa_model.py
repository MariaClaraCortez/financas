from src.database.conexao import Conexao

class Despesa:
    def __init__(self):
        pass

    @staticmethod
    def incluir(login:str,id_categoria:int,descricao:str,valor:float,data:str) -> int:
        conexao,cursor = Conexao().conectar()
        
        if not conexao:
            print("ERRO AO TENTAR CONECTAR")
            return None
        
        try:
            cursor.execute("""
                            INSERT INTO tb_despesas (login,id_categoria,descricao,valor,data) 
                        VALUES (%s,%s,%s,%s,%s)
                        """,
                        [login,id_categoria,descricao,valor,data])
            id_despesa = cursor.lastrowid
            conexao.commit()
            conexao.close()
            return id_despesa
        except Exception as erro:
            print(f"ERRO AO INSERIR: {erro}")
            return None
        
    
    @staticmethod
    def recuperar_todos (login:str) -> list[dict]:
        conexao,cursor = Conexao().conectar()

        if not conexao:
            print("ERRO AO TENTAR CONECTAR")
            return None
        
        try:
            cursor.execute("""
                            SELECT tb_despesas.login,tb_categorias.tipo,tb_despesas.descricao,tb_despesas.valor,tb_despesas.data from tb_despesas
                            inner join tb_categorias on tb_categorias.id_categoria = tb_despesas.id_categoria
                            WHERE tb_despesas.login = %s
                        """,[login])
            
            dados = cursor.fetchall()
            conexao.close()
            return dados
        except Exception as erro:
            print(f"ERRO AO INSERIR: {erro}")
            return None
        

    @staticmethod
    def recuperar_por_categoria (login:str, id_categoria:int) -> list[dict]:
        conexao,cursor = Conexao().conectar()

        if not conexao:
            print("ERRO AO TENTAR CONECTAR")
            return None
        
        try:
            cursor.execute("""
                            SELECT login,id_categoria,descricao,valor,data from tb_despesas
                           WHERE login = %s AND id_categoria = %s
                        """,[login,id_categoria])
            
            dados = cursor.fetchall()
            conexao.close()
            return dados
        except Exception as erro:
            print(f"ERRO AO INSERIR: {erro}")
            return None
        
    

    @staticmethod
    def excluir (id_despesa:int) -> bool:
        conexao,cursor = Conexao().conectar()

        if not conexao:
            print("ERRO AO CONECTAR")
            return False
        try:
            cursor.execute("""
                            DELETE FROM tb_despesas WHERE id_despesa = %s
                        """,[id_despesa])
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro:
            print(f"ERRO AO EXCLUIR: {erro}")
            return False


    @staticmethod
    def alterar(id_despesa:int,login:str,id_categoria:int,descricao:str,valor:float,data:str) -> bool:
        conexao,cursor = Conexao().conectar()
        
        if not conexao:
            print("ERRO AO TENTAR CONECTAR")
            return False
        
        try:
            cursor.execute("""
                            UPDATE tb_despesas SET id_categoria = %s,
                           descricao = %s,
                           valor = %s,
                           data = %s,
                           WHERE
                           id_despesa = %s
                           AND login = %s;
                        """,
                        [id_categoria,descricao,valor,data,id_despesa,login])
            id = cursor.lastrowid
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro:
            print(f"ERRO AO INSERIR: {erro}")
            return False