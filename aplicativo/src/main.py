from PySide2 import ( QtCore, QtGui, QtWidgets )
from interfaceConfigs.mainConfig.main import ( Ui_DescomplicadaMente )
from controllers.SessionController import ( loga )
from functions.alter_screen import ( mudarTela )
from interfaceConfigs.homeConfig.main import *
from interfaceConfigs.homeConfig.emotion import *
from interfaceConfigs.homeConfig.content import *
from interfaceConfigs.homeConfig.feed import *
from interfaceConfigs.homeConfig.styles import *

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_DescomplicadaMente()
    ui.setupUi(MainWindow)


    loga(ui)
    alterarQuadro(ui)
    configEmoções(ui)
    configConteudos(ui)
    configFeed(ui)
    alterarEstilo(ui)

    MainWindow.show()

    mudarTela(ui)

    alterarQuadro(ui)

    sys.exit(app.exec_())

#Login de teste
#gabriel@hotmail.com
#senhordosaneis