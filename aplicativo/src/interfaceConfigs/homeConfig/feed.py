from PySide2 import QtWidgets
from PySide2.QtCore import Slot, QCoreApplication

_translate = QCoreApplication.translate

'''
    CONFIGURAÇÃO DO QUADRO DE FEED
'''

def configFeed(ui):

    ui.btnLer = QtWidgets.QPushButton(ui.verticalLayoutWidget_6)
    ui.btnLer.setObjectName('btnLer')
    ui.btnLer.setStyleSheet('background-color: #00ffff;')
    ui.btnLer.setText(_translate('DescomplicadaMente', 'Ler Mais'))
    ui.layConteudo.addWidget(ui.btnLer)