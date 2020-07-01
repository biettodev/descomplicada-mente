from PySide2.QtCore import Slot
from PySide2 import QtWidgets

'''
    CONFIGURAÇÃO DOS BOTÕES DAS EMOÇÕES
'''

def configEmoções(ui):

    def config():

        ui.btnRaiva = QtWidgets.QPushButton(ui.horizontalLayoutWidget)
        ui.btnRaiva.setText('Raiva')
        ui.sclaOpcoes.addWidget(ui.btnRaiva)

    @Slot()
    def abreEmoções():
        ui.opcoes.raise_()

    ui.btnConteudos.clicked.connect(abreEmoções)
