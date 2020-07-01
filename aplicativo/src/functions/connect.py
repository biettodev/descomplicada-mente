import mysql.connector

def connection():
    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'usbw',
            database = 'dm'
                                )
        print('Conexão com Banco de Dados criada.')
        return conn
    except mysql.connector.Error:
        print('Não foi possível acessar o banco.')
        return False
