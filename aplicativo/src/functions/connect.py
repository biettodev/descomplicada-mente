import mysql.connector

def connection():
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'usbw',
        database = 'ds'
                            )
    if conn:
        return conn
        print('Conectado ao Banco de Dados com sucesso.')
    else:
        print('Erro com Banco de Dados.')
