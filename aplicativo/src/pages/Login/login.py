from mainUi import Ui_DescomplicadaMente
from functions.connect import connection
from PySide2.QtCore import Slot

conn = connection()
cursor = conn.cursor()

def loga(ui):

    @Slot()
    def ir_home():
        ui.home.raise_()

    def logar():

        u_email = str(ui.lnEmail.text())
        u_senha = str(ui.lnSenha.text())

        select = (f"SELECT * FROM `users` WHERE `email` = %s AND `senha` = %s")
        result = cursor.execute(select, (u_email, u_senha))
        t = cursor.fetchone()
        print(f'Pessoa: {t}')
        if len(t) > 0:
            for v in t:
                print(v)
                ui.btnEntrar.clicked.connect(ir_home())
        else:
            print('Usuário não encontrado')

    ui.btnEntrar.clicked.connect(logar)
