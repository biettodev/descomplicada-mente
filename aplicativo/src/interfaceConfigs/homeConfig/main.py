from interfaceConfigs.mainConfig.main import Ui_DescomplicadaMente
from PySide2 import ( QtWidgets) 
from PySide2.QtCore import ( Slot )
import webbrowser

openedCont = True
def alterarQuadro(ui):

    '''
        CONFIGURAÇÃO DOS BOTÕES QUE ALTERAM O QUADRO DE EXIBIÇÃO
    '''

    

    @Slot()
    def abrirFeed():
        ui.sclaFeed.raise_()    

    @Slot()
    def abrirConteúdos():
        global openedCont
        if not openedCont:
            print('Clicou em conteúdos')
            ui.sclaConteudos.raise_()
            ui.opcoes_2.raise_()
            openedCont = True

    @Slot()
    def abrirBiblioteca():
        ui.sclaBiblioteca.raise_()

    @Slot()
    def abrirNotificações():
        ui.sclaNotificacao.raise_()
        
    @Slot()
    def abrirEmoções():
        global openedCont
        if openedCont:
            print('Clicou em emoções')
            ui.opcoes_2.raise_()
            openedCont = False

    @Slot()
    def abrirChat():
        webbrowser.open('https://sociedadeamigosdavida.org.br/Chatonline/', new='1')
        
    ui.btnHome.clicked.connect(abrirFeed)

    ui.btnConteudos.clicked.connect(abrirConteúdos)

    ui.btnBiblioteca.clicked.connect(abrirBiblioteca)

    ui.btnNotifica.clicked.connect(abrirNotificações)
    
    ui.btnEmocoes.clicked.connect(abrirEmoções)
    
    ui.btnChat.clicked.connect(abrirChat)
