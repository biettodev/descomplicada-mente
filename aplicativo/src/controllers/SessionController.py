from interfaceConfigs.mainConfig.main import Ui_DescomplicadaMente

from functions.connect import connection
from functions.sessions import Session

from PySide2.QtCore import Slot

from time import sleep

conn = connection()
if conn != False:
    cursor = conn.cursor()
else:
    cursor = False

def loga(ui):

    @Slot()
    def ir_home(ui):
        ui.home.raise_()

    def createSession(login, email, senha):
        if login:
            print('Sessão criada')
            return(email, senha)

    def logar():

        u_email = str(ui.lnEmail.text())

        u_senha = str(ui.lnSenha.text())

        select = (f'SELECT * FROM `usuarios` WHERE `email` = %s AND `senha` = %s')
        
        try:
            result = cursor.execute(select, (u_email, u_senha))
            t = cursor.fetchone()
        except:
            print('Não foi possível buscar os dados. Verifique sua conexão com o servidor')
            sleep(7)
            quit()
        

        if t != None:
            logado = True
            session = createSession(logado, u_email, u_senha)
            print(session)
            ir_home(ui)

        else:
            print('Os dados não são válidos.')

    ui.btnEntrar.clicked.connect(logar)