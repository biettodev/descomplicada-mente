from functions.funcoes import getMovies
from mainUi import Ui_DescomplicadaMente
from PySide2 import QtWidgets
from PySide2.QtCore import Slot, QCoreApplication
from functions import funcoes

_translate = QCoreApplication.translate


'''
    FUNÇÃO QUE ALTERA O CSS DE ACORDO COM A EMOÇÃO SELECIONADA
'''

def alterarEstilo(ui):

    def estilizar():
        estilo = '''
            QFrame {
                background: #2888ff;
            }
            QPushButton {
                background: #2e2eff;
            }
        '''
        ui.home.setStyleSheet(estilo)


    ui.btnRaiva.clicked.connect(estilizar)


'''
    CONFIGURAÇÃO DOS BOTÕES QUE ALTERAM O QUADRO DE EXIBIÇÃO
'''

def alterarQuadro(ui):

    @Slot()
    def abrirFeed():
        ui.sclaFeed.raise_()

    @Slot()
    def abrirConteúdos():
        ui.sclaConteudos.raise_()
        ui.opcoes_2.raise_()

    @Slot()
    def abrirBiblioteca():
        ui.sclaBiblioteca.raise_()

    @Slot()
    def abrirNotificações():
        ui.sclaNotificacao.raise_()

    ui.btnHome.clicked.connect(abrirFeed)

    ui.btnConteudos.clicked.connect(abrirConteúdos)

    ui.btnBiblioteca.clicked.connect(abrirBiblioteca)

    ui.btnNotifica.clicked.connect(abrirNotificações)


'''
    CONFIGURAÇÃO DOS BOTÕES DAS EMOÇÕES
'''

def configEmoções(ui):

    def config():

        ui.btnRaiva = QtWidgets.QPushButton(ui.horizontalLayoutWidget)
        ui.btnRaiva.setText('Raiva')
        ui.sclaOpcoes.addWidget(ui.btnRaiva)

        print('Menu Emoções configurado')

    @Slot()
    def abreEmoções():
        ui.opcoes.raise_()

    ui.btnConteudos.clicked.connect(abreEmoções)

'''
    CONFIGURAÇÃO DO QUADRO DE FEED
'''

def configFeed(ui):
    ui.btnLer = QtWidgets.QPushButton(ui.verticalLayoutWidget_6)
    ui.btnLer.setObjectName('btnLer')
    ui.btnLer.setStyleSheet('background-color: #00ffff;')
    ui.btnLer.setText(_translate('DescomplicadaMente', 'Ler Mais'))
    ui.layConteudo.addWidget(ui.btnLer)
    print('Quadro Notícias configurado')

'''
    CONFIGURAÇÃO DO QUADRO DE CONTEÚDOS
'''

def configConteudos(ui):

    ui.groupBox = QtWidgets.QGroupBox('<font color=white>Teste</font>')

    moviesList = getMovies()

    labelList = list()
    buttonList = list()

    for i, f in enumerate(moviesList):
        ui.lbTitulo = QtWidgets.QLabel(ui.verticalLayoutWidget_7)
        ui.lbTitulo.setText(f'<font color=white align=center>{f[1]}</font>')
        labelList.append(ui.lbTitulo)

        ui.btnAdicionar = QtWidgets.QPushButton(ui.verticalLayoutWidget_7)
        ui.btnAdicionar.setStyleSheet('background-color: #00ffff;')
        ui.btnAdicionar.setText('Adicionar')
        buttonList.append(ui.btnAdicionar)

        ui.layConteudo_2.addWidget(labelList[i])
        ui.layConteudo_2.addWidget(buttonList[i])
    print('Quadro Conteúdos configurado')

    ui.groupBox.setLayout(ui.layConteudo_2)
    ui.sclaConteudos.setWidget(ui.groupBox)
    ui.sclaConteudos.setFixedHeight(300)

'''
    CONFIGURAÇÃO DO QUADRO DE NOTIFICAÇÕES
'''

def notificacao(ui):
    print('Menu Notificações configurado')