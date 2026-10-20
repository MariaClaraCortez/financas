import mysql.connector

class Conexao:
    def __init__(self):
        pass


    @staticmethod
    def conectar():
        try:
            #criar a conexao com o banco de dados mysql
            conexao = mysql.connector.connect(
                host="localhost",
                port= 3306,
                user = "root",
                password="root",
                database = "financas"
            )

            cursor = conexao.cursor()

            return conexao, cursor
        except BaseException as erro:
            print (f"ERRO: {erro}")
            return None,None


