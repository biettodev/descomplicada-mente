from ds import *
from PySide2.QtCore import Slot

def mudarTela(ui):
    @Slot()
    def ir_login():
        ui.login.raise_()

    @Slot()
    def ir_home():
        ui.home.raise_()

    ui.btnEntrar.clicked.connect(ir_home)
    ui.btnLogout.clicked.connect(ir_login)
