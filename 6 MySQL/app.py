import mysql.connector
from mysql.connector import Error

def conectar():
    """Estabelece conecção com o BD"""
    try:
        conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            database = "pythonex"
        )
        if conexao.is_connected():
            print("Conexão realizada com sucesso!")
            return conexao
    except Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None

