from PySide2 import QtCore, QtGui, QtWidgets
from mainUi import Ui_DescomplicadaMente

from pages.Login.login import loga
from pages.Home.home import configEmoções, configConteudos, configFeed, alterarEstilo, alterarQuadro

from functions.alter_screen import mudarTela

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_DescomplicadaMente()
    ui.setupUi(MainWindow)

    configEmoções(ui)
    configConteudos(ui)
    configFeed(ui)
    alterarEstilo(ui)

    MainWindow.show()

    mudarTela(ui)
    loga(ui)
    alterarQuadro(ui)

    sys.exit(app.exec_())

#Login de teste
#gabriel@hotmail.com
#senhordosaneis