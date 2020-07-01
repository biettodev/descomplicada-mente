from interfaceConfigs.mainConfig.main import Ui_DescomplicadaMente
from PySide2.QtCore import Slot

def mudarTela(ui):
    
    @Slot()
    def ir_login():
        ui.login.raise_()

    ui.btnLogout.clicked.connect(ir_login)
