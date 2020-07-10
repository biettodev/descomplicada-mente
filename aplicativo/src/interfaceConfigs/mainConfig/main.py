# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUi.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from interfaceConfigs.basicConfig.main import *

import resources.principal_rc

class Ui_DescomplicadaMente(object):
    def setupUi(self, DescomplicadaMente):
        if not DescomplicadaMente.objectName():
            DescomplicadaMente.setObjectName(u"DescomplicadaMente")
        # WINDOW
        DescomplicadaMente.resize(500, 550)
        DescomplicadaMente.setMinimumSize(QSize(500, 550))
        DescomplicadaMente.setMaximumSize(QSize(500, 550))
        icon = QIcon()
        icon.addFile(u":/logo/logo-cerebro.png", QSize(), QIcon.Normal, QIcon.Off)
        DescomplicadaMente.setWindowIcon(icon)
        DescomplicadaMente.setStyleSheet(u"QFrame{\n"
"	text-align: center;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"	border-radius: 3px;\n"
"	background-color: rgb(0, 240, 240);\n"
"	padding: 6px;\n"
"	margin: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 255, 255)\n"
"}\n"
"QWidgets{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        # CENTRAL WIDGET
        self.centralwidget = QWidget(DescomplicadaMente)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(500, 550))
        self.centralwidget.setMaximumSize(QSize(500, 550))
        
        # HOME
        self.home = QFrame(self.centralwidget)
        self.home.setObjectName(u"home")
        self.home.setGeometry(QRect(0, 0, 500, 550))
        self.home.setMinimumSize(QSize(500, 550))
        self.home.setMaximumSize(QSize(500, 550))
        self.home.setStyleSheet(u"*{\n"
"	font: 10pt \"Sitka Text\";\n"
"	background-color: rgb(13,13, 13);\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(85, 255, 255);\n"
"	border-radius: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(65, 230, 230);\n"
"}")
        self.home.setFrameShape(QFrame.StyledPanel)
        self.home.setFrameShadow(QFrame.Raised)
        self.wdConteudo = QWidget(self.home)
        self.wdConteudo.setObjectName(u"wdConteudo")
        self.wdConteudo.setGeometry(QRect(9, 120, 420, 382))
        self.wdConteudo.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 7px;")

        # FEED CONTENT
        self.sclaFeed = QScrollArea(self.wdConteudo)

        self.scrollAreaWidgetContents_2 = QWidget()
        
        self.verticalLayoutWidget_6 = QWidget(self.scrollAreaWidgetContents_2)
        
        self.layConteudo = QVBoxLayout(self.verticalLayoutWidget_6) 
        
        contentBoardConfig(self.sclaFeed, u"sclaFeed", self.scrollAreaWidgetContents_2, u"scrollAreaWidgetContents_2", self.verticalLayoutWidget_6, u"verticalLayoutWidget_6", self.layConteudo, u"layConteudo")
        
        # MAIN CONTENT
        self.sclaConteudos = QScrollArea(self.wdConteudo)
             
        self.scrollAreaWidgetContents_3 = QWidget()
        
        self.verticalLayoutWidget_7 = QWidget(self.scrollAreaWidgetContents_3)
        
        self.layConteudo_2 = QVBoxLayout(self.verticalLayoutWidget_7)
        
        contentBoardConfig(self.sclaConteudos, u"sclaConteudos", self.scrollAreaWidgetContents_3, u"scrollAreaWidgetContents_3", self.verticalLayoutWidget_7, u"verticalLayoutWidget_7", self.layConteudo_2, u"layConteudo_2")
        
        # self.verticalLayoutWidget_7.setGeometry(QRect(0, 0 100, 100))
        
        # NOTIFY CONTENT
        self.sclaNotificacao = QScrollArea(self.wdConteudo)

        self.scrollAreaWidgetContents_4 = QWidget()

        self.horizontalLayoutWidget_3 = QWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_3)
        
        contentBoardConfig(self.sclaNotificacao, u"sclaNotificacao", self.scrollAreaWidgetContents_4, u"scrollAreaWidgetContents_3", self.horizontalLayoutWidget_3, u"horizontalLayoutWidget_3", self.horizontalLayout, u"horizontalLayout")
        
        # LIBRARY CONTENT
        self.sclaBiblioteca = QScrollArea(self.wdConteudo)
        self.sclaBiblioteca.setObjectName(u"sclaBiblioteca")
        self.sclaBiblioteca.setGeometry(QRect(0, 0, 420, 381))
        self.sclaBiblioteca.setStyleSheet(u"")
        self.sclaBiblioteca.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.sclaBiblioteca.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.sclaBiblioteca.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 420, 381))
        self.verticalLayoutWidget_9 = QWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(10, 10, 420, 151))
        self.layConteudo_3 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.layConteudo_3.setSpacing(3)
        self.layConteudo_3.setObjectName(u"layConteudo_3")
        self.layConteudo_3.setContentsMargins(0, 0, 0, 0)
        self.sclaBiblioteca.setWidget(self.scrollAreaWidgetContents_5)
        
        # ORDER CONTENT
        self.sclaFeed.raise_()
        self.sclaBiblioteca.raise_()
        self.sclaConteudos.raise_()
        self.sclaNotificacao.raise_()
        
        # HOME MENU
        self.horizontalLayoutWidget_5 = QWidget(self.home)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(0, 510, 500, 44))
        self.layMenu_2 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.layMenu_2.setObjectName(u"layMenu_2")
        self.layMenu_2.setContentsMargins(0, 0, 0, 0)
        
        self.btnHome = QPushButton(self.horizontalLayoutWidget_5)
        icon1 = QIcon()
        self.btnHome.setIconSize(QSize(20, 20))
        buttonConfig(self.btnHome, u"btnHome", icon1, u":/icons/home.png", self.layMenu_2)

        self.btnBiblioteca = QPushButton(self.horizontalLayoutWidget_5)
        icon2 = QIcon()
        self.btnBiblioteca.setIconSize(QSize(20, 20))
        buttonConfig(self.btnBiblioteca, u"btnBiblioteca", icon2, u":/icons/biblioteca.png", self.layMenu_2)
        
        # MAIN MENU
        self.wdMenuPrincipal = QWidget(self.home)
        self.wdMenuPrincipal.setObjectName(u"wdMenuPrincipal")
        self.wdMenuPrincipal.setGeometry(QRect(0, 0, 500, 71))
        self.wdMenuPrincipal.setStyleSheet(u"*{\n"
"	background-color: rgb(30, 30, 30);\n"
"	border-radius: 7px;\n"
"	text-transform: uppercase;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(85, 255, 255);\n"
"	border-radius: 3px;\n"
"}")
        self.horizontalLayoutWidget = QWidget(self.wdMenuPrincipal)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 500, 44))
        self.layMenuHome = QHBoxLayout(self.horizontalLayoutWidget)
        self.layMenuHome.setSpacing(2)
        self.layMenuHome.setObjectName(u"layMenuHome")
        self.layMenuHome.setContentsMargins(0, 0, 0, 0)
        
        self.btnConteudos = QPushButton(self.horizontalLayoutWidget)
        self.btnConteudos.setEnabled(True)
        icon3 = QIcon()
        self.btnConteudos.setIconSize(QSize(18, 18))
        buttonConfig(self.btnConteudos, u"btnConteudos", icon3, u":/icons/conteudo.png", self.layMenuHome)
        
        self.btnEmocoes = QPushButton(self.horizontalLayoutWidget)
        icon4 = QIcon()
        self.btnEmocoes.setIconSize(QSize(18, 18))
        buttonConfig(self.btnEmocoes, u"btnEmocoes", icon4, u":/icons/emocoes.png", self.layMenuHome)

        self.btnLogout = QPushButton(self.horizontalLayoutWidget)
        icon5 = QIcon()
        self.btnLogout.setIconSize(QSize(18, 18))
        buttonConfig(self.btnLogout, u"btnLogout", icon5, u":/icons/login.png", self.layMenuHome)

        # EMOTIONS MENU
        self.opcoes = QFrame(self.wdMenuPrincipal)
        frameConfig(self.opcoes, u"opcoes", 0, 40, 500, 31)
        
        self.horizontalLayoutWidget_2 = QWidget(self.opcoes)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, -10, 500, 51))
        self.layOpcoes = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.layOpcoes.setSpacing(3)
        self.layOpcoes.setObjectName(u"layOpcoes")
        self.layOpcoes.setContentsMargins(0, 0, 0, 0)
        
        self.btnRaiva = QPushButton(self.horizontalLayoutWidget_2)
        iconRaiva = QIcon()
        buttonConfig(self.btnRaiva, u"btnRaiva", iconRaiva, u":/icons/angry-solid.svg", self.layOpcoes)

        self.btnTristeza = QPushButton(self.horizontalLayoutWidget_2)
        iconTriste = QIcon()
        buttonConfig(self.btnTristeza, u"btnTristeza", iconTriste, u":/icons/sad-tear-solid.svg", self.layOpcoes)

        self.btnDesespero = QPushButton(self.horizontalLayoutWidget_2)
        iconDesesp = QIcon()
        buttonConfig(self.btnDesespero, u"btnDesespero", iconDesesp, u":/icons/tired-solid.svg", self.layOpcoes)
        
        # CONTENTS MENU
        self.opcoes_2 = QFrame(self.wdMenuPrincipal)
        frameConfig(self.opcoes_2, u"opcoes_2", 0, 40, 500, 31)
        
        self.horizontalLayoutWidget_4 = QWidget(self.opcoes_2)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(0, -10, 500, 51))
        self.layOpcoes_2 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.layOpcoes_2.setSpacing(3)
        self.layOpcoes_2.setObjectName(u"layOpcoes_2")
        self.layOpcoes_2.setContentsMargins(0, 0, 0, 0)   
        
        self.btnFilmes = QPushButton(self.horizontalLayoutWidget_4)
        icon10 = QIcon()
        buttonConfig(self.btnFilmes, u"btnFilmes", icon10, u":/icons/film-solid.svg", self.layOpcoes_2)

        self.btnArtigos = QPushButton(self.horizontalLayoutWidget_4)
        icon11 = QIcon()
        buttonConfig(self.btnArtigos, u"btnArtigos", icon11, u":/icons/newspaper-regular.svg", self.layOpcoes_2)

        self.btnLivros = QPushButton(self.horizontalLayoutWidget_4)
        icon12 = QIcon()
        buttonConfig(self.btnLivros, u"btnLivros", icon12, u":/icons/book-solid.svg", self.layOpcoes_2)

        self.btnCanais = QPushButton(self.horizontalLayoutWidget_4)
        icon13 = QIcon()
        buttonConfig(self.btnCanais, u"btnCanais", icon13, u":/icons/video-solid.svg", self.layOpcoes_2)
        
        self.opcoes.raise_()
        self.horizontalLayoutWidget.raise_()
        self.opcoes_2.raise_()
        
        # SIDEBAR
        self.wdSidebar = QWidget(self.home)
        self.wdSidebar.setObjectName(u"wdSidebar")
        self.wdSidebar.setGeometry(QRect(436, 80, 60, 420))
        self.wdSidebar.setStyleSheet(u"*{\n"
"	background-color: rgb(30, 30, 30);\n"
"	border-radius: 7px;\n"
"}\n"
"QPushButton{\n"
"	background-color: rgb(85, 255, 255);\n"
"	border-radius: 3px;\n"
"}")
        self.verticalLayoutWidget_8 = QWidget(self.wdSidebar)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(0, 30, 60, 330))
        self.laySidebar = QVBoxLayout(self.verticalLayoutWidget_8)
        self.laySidebar.setObjectName(u"laySidebar")
        self.laySidebar.setContentsMargins(0, 0, 0, 0)
        
        self.btnNotifica = QPushButton(self.verticalLayoutWidget_8)
        icon7 = QIcon()
        buttonConfig(self.btnNotifica, u"btnNotifica", icon7, u":/icons/notificacao.png", self.laySidebar)
        
        self.btnChat = QPushButton(self.verticalLayoutWidget_8)
        icon9 = QIcon()
        buttonConfig(self.btnChat, u"btnChat", icon9, u":/icons/chat.svg", self.laySidebar)
        
        # PESQUISAR ITEM
        self.wdPesquisar = QWidget(self.home)
        self.wdPesquisar.setObjectName(u"wdPesquisar")
        self.wdPesquisar.setGeometry(QRect(0, 80, 400, 32))
        self.formLayoutWidget = QWidget(self.wdPesquisar)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 0, 400, 32))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.btnPesquisar = QPushButton(self.formLayoutWidget)
        self.btnPesquisar.setMinimumSize(QSize(80, 32))
        self.btnPesquisar.setMaximumSize(QSize(80, 32))
        self.btnPesquisar.setObjectName(u"btnPesquisar")
        self.btnPesquisar.setStyleSheet(u"*{\n"
"	background-color: rgb(30, 30, 30);\n"
"	border-radius: 7px;\n"
"	color: rgb(85, 255, 255)\n"
"}")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.btnPesquisar)
        self.lnPesquisar = QLineEdit(self.formLayoutWidget)
        self.lnPesquisar.setMinimumSize(QSize(300, 32))
        self.lnPesquisar.setMaximumSize(QSize(300, 32))
        self.lnPesquisar.setObjectName(u"lnPesquisar")
        self.lnPesquisar.setStyleSheet(u"*{\n"
"	background-color: rgb(30, 30, 30);\n"
"	border-radius: 7px;\n"
"	color: rgb(85, 255, 255);\n"
"	height: 18px;\n"
"	padding: 5px;\n"
"}")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lnPesquisar)

        # LOGIN
        self.login = QFrame(self.centralwidget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(0, 0, 500, 550))
        self.login.setMinimumSize(QSize(500, 550))
        self.login.setMaximumSize(QSize(500, 350))
        self.login.setStyleSheet(u"*{\n"
"	background-color: rgb(255, 123, 150);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: none;\n"
"	border-bottom: 2px solid #FFF;\n"
"	padding: 3px;\n"
"	margin: 0 5px;\n"
"	font-size: 13px;\n"
"	font-weight: 500;\n"
"	color: #FFF;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: #FFF;\n"
"	background-color: rgb(90, 57, 148);\n"
"	height: 30px;\n"
"	max-width: 300px;\n"
"	border-radius: 0;\n"
"	margin: 0 6px;\n"
"	font: 15pt \"NSimSun\";\n"
"}")
        self.login.setFrameShape(QFrame.StyledPanel)
        self.login.setFrameShadow(QFrame.Raised)
        self.frLogo = QFrame(self.login)
        self.frLogo.setObjectName(u"frLogo")
        self.frLogo.setGeometry(QRect(0, -100, 500, 700))
        self.frLogo.setStyleSheet(u"QFrame{\n"
"	image: url(:/logo/logo-cerebro.png);\n"
"}\n"
"")
        self.frLogo.setFrameShape(QFrame.StyledPanel)
        self.frLogo.setFrameShadow(QFrame.Raised)
        
        self.verticalLayoutWidget = QWidget(self.login)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(120, 370, 260, 130))
        self.layLogin = QVBoxLayout(self.verticalLayoutWidget)
        self.layLogin.setSpacing(15)
        self.layLogin.setObjectName(u"layLogin")
        self.layLogin.setContentsMargins(0, 0, 0, 0)
        
        self.lnEmail = QLineEdit(self.verticalLayoutWidget)
        self.lnEmail.setObjectName(u"lnEmail")
        self.lnEmail.setFocusPolicy(Qt.ClickFocus)
        self.lnEmail.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.layLogin.addWidget(self.lnEmail)

        self.lnSenha = QLineEdit(self.verticalLayoutWidget)
        self.lnSenha.setObjectName(u"lnSenha")
        self.lnSenha.setFocusPolicy(Qt.ClickFocus)
        self.lnSenha.setEchoMode(QLineEdit.Password)
        self.lnSenha.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.layLogin.addWidget(self.lnSenha)

        self.btnEntrar = QPushButton(self.verticalLayoutWidget)
        self.btnEntrar.setObjectName(u"btnEntrar")
        icon8 = QIcon()
        icon8.addFile(u"../assets/icones/login.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEntrar.setIcon(icon8)
        self.btnEntrar.setIconSize(QSize(20, 20))

        self.layLogin.addWidget(self.btnEntrar)

        # ORDEM DE TABULAÇÃO
        DescomplicadaMente.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.sclaFeed, self.sclaConteudos)
        QWidget.setTabOrder(self.sclaConteudos, self.sclaNotificacao)
        QWidget.setTabOrder(self.sclaNotificacao, self.sclaBiblioteca)
        QWidget.setTabOrder(self.sclaBiblioteca, self.btnHome)
        QWidget.setTabOrder(self.btnHome, self.btnBiblioteca)
        QWidget.setTabOrder(self.btnBiblioteca, self.btnConteudos)
        QWidget.setTabOrder(self.btnConteudos, self.btnEmocoes)
        QWidget.setTabOrder(self.btnEmocoes, self.btnLogout)
        QWidget.setTabOrder(self.btnLogout, self.btnRaiva)
        QWidget.setTabOrder(self.btnRaiva, self.btnDesespero)
        QWidget.setTabOrder(self.btnDesespero, self.btnTristeza)
        QWidget.setTabOrder(self.btnTristeza, self.btnFilmes)
        QWidget.setTabOrder(self.btnFilmes, self.btnArtigos)
        QWidget.setTabOrder(self.btnArtigos, self.btnLivros)
        QWidget.setTabOrder(self.btnLivros, self.btnCanais)
        QWidget.setTabOrder(self.btnCanais, self.btnNotifica)

        self.retranslateUi(DescomplicadaMente)

        QMetaObject.connectSlotsByName(DescomplicadaMente)
    # setupUi

    def retranslateUi(self, DescomplicadaMente):
        DescomplicadaMente.setWindowTitle(QCoreApplication.translate("DescomplicadaMente", u"Descomplicada Mente", None))
        self.btnHome.setText(QCoreApplication.translate("DescomplicadaMente", u"Home", None))
        self.btnBiblioteca.setText(QCoreApplication.translate("DescomplicadaMente", u"Biblioteca", None))
        self.btnConteudos.setText(QCoreApplication.translate("DescomplicadaMente", u"Conte\u00fados", None))
        self.btnEmocoes.setText(QCoreApplication.translate("DescomplicadaMente", u"Emo\u00e7\u00f5es", None))
        self.btnLogout.setText(QCoreApplication.translate("DescomplicadaMente", u"Sair", None))
        self.btnRaiva.setText(QCoreApplication.translate("DescomplicadaMente", u"Raiva", None))
        self.btnTristeza.setText(QCoreApplication.translate("DescomplicadaMente", u"Tristeza", None))
        self.btnDesespero.setText(QCoreApplication.translate("DescomplicadaMente", u"Desespero", None))
        self.btnFilmes.setText(QCoreApplication.translate("DescomplicadaMente", u"Filmes", None))
        self.btnArtigos.setText(QCoreApplication.translate("DescomplicadaMente", u"Artigos", None))
        self.btnLivros.setText(QCoreApplication.translate("DescomplicadaMente", u"Livros", None))
        self.btnCanais.setText(QCoreApplication.translate("DescomplicadaMente", u"Canais", None))
        self.btnNotifica.setText("")
        self.btnPesquisar.setText(QCoreApplication.translate("DescomplicadaMente", u"Pesquisar", None))
        self.lnEmail.setPlaceholderText(QCoreApplication.translate("DescomplicadaMente", u"Email", None))
        self.lnSenha.setPlaceholderText(QCoreApplication.translate("DescomplicadaMente", u"Senha", None))
        self.btnEntrar.setText(QCoreApplication.translate("DescomplicadaMente", u"Entrar", None))
    # retranslateUi

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()

    ui = Ui_DescomplicadaMente()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    
    sys.exit(app.exec_())

