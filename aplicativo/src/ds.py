# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ds.ui'
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

import resources.principal_rc

class Ui_DescomplicadaMente(object):
    def setupUi(self, DescomplicadaMente):
        if not DescomplicadaMente.objectName():
            DescomplicadaMente.setObjectName(u"DescomplicadaMente")
        DescomplicadaMente.resize(360, 550)
        DescomplicadaMente.setMinimumSize(QSize(360, 550))
        DescomplicadaMente.setMaximumSize(QSize(360, 550))
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
        self.centralwidget = QWidget(DescomplicadaMente)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(360, 550))
        self.centralwidget.setMaximumSize(QSize(360, 550))
        self.home = QFrame(self.centralwidget)
        self.home.setObjectName(u"home")
        self.home.setGeometry(QRect(0, 0, 360, 550))
        self.home.setMinimumSize(QSize(360, 550))
        self.home.setMaximumSize(QSize(360, 550))
        self.home.setStyleSheet(u"*{\n"
"	font: 8pt \"Sitka Text\";\n"
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
        self.wdConteudo.setGeometry(QRect(9, 120, 291, 381))
        self.wdConteudo.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 7px;")
        self.sclaFeed = QScrollArea(self.wdConteudo)
        self.sclaFeed.setObjectName(u"sclaFeed")
        self.sclaFeed.setGeometry(QRect(0, 0, 281, 381))
        self.sclaFeed.setStyleSheet(u"")
        self.sclaFeed.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.sclaFeed.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.sclaFeed.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 281, 381))
        self.verticalLayoutWidget_6 = QWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 10, 301, 151))
        self.layConteudo = QVBoxLayout(self.verticalLayoutWidget_6)
        self.layConteudo.setObjectName(u"layConteudo")
        self.layConteudo.setContentsMargins(0, 0, 0, 0)
        self.sclaFeed.setWidget(self.scrollAreaWidgetContents_2)
        self.sclaConteudos = QScrollArea(self.wdConteudo)
        self.sclaConteudos.setObjectName(u"sclaConteudos")
        self.sclaConteudos.setGeometry(QRect(0, 0, 291, 381))
        self.sclaConteudos.setStyleSheet(u"")
        self.sclaConteudos.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.sclaConteudos.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.sclaConteudos.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 291, 381))
        self.verticalLayoutWidget_7 = QWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(10, 10, 301, 151))
        self.layConteudo_2 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.layConteudo_2.setObjectName(u"layConteudo_2")
        self.layConteudo_2.setContentsMargins(0, 0, 0, 0)
        self.sclaConteudos.setWidget(self.scrollAreaWidgetContents_3)
        self.sclaNotificacao = QScrollArea(self.wdConteudo)
        self.sclaNotificacao.setObjectName(u"sclaNotificacao")
        self.sclaNotificacao.setGeometry(QRect(0, 0, 291, 381))
        self.sclaNotificacao.setStyleSheet(u"")
        self.sclaNotificacao.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.sclaNotificacao.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.sclaNotificacao.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 291, 381))
        self.horizontalLayoutWidget_3 = QWidget(self.scrollAreaWidgetContents_4)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 10, 301, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sclaNotificacao.setWidget(self.scrollAreaWidgetContents_4)
        self.sclaBiblioteca = QScrollArea(self.wdConteudo)
        self.sclaBiblioteca.setObjectName(u"sclaBiblioteca")
        self.sclaBiblioteca.setGeometry(QRect(0, 0, 291, 381))
        self.sclaBiblioteca.setStyleSheet(u"")
        self.sclaBiblioteca.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.sclaBiblioteca.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.sclaBiblioteca.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 291, 381))
        self.verticalLayoutWidget_9 = QWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(10, 10, 271, 151))
        self.layConteudo_3 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.layConteudo_3.setSpacing(3)
        self.layConteudo_3.setObjectName(u"layConteudo_3")
        self.layConteudo_3.setContentsMargins(0, 0, 0, 0)
        self.sclaBiblioteca.setWidget(self.scrollAreaWidgetContents_5)
        self.sclaConteudos.raise_()
        self.sclaNotificacao.raise_()
        self.sclaFeed.raise_()
        self.sclaBiblioteca.raise_()
        self.horizontalLayoutWidget_5 = QWidget(self.home)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(0, 510, 361, 44))
        self.layMenu_2 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.layMenu_2.setObjectName(u"layMenu_2")
        self.layMenu_2.setContentsMargins(0, 0, 0, 0)
        self.btnHome = QPushButton(self.horizontalLayoutWidget_5)
        self.btnHome.setObjectName(u"btnHome")
        icon1 = QIcon()
        icon1.addFile(u":/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnHome.setIcon(icon1)
        self.btnHome.setIconSize(QSize(20, 20))

        self.layMenu_2.addWidget(self.btnHome)

        self.btnBiblioteca = QPushButton(self.horizontalLayoutWidget_5)
        self.btnBiblioteca.setObjectName(u"btnBiblioteca")
        icon2 = QIcon()
        icon2.addFile(u":/icons/biblioteca.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnBiblioteca.setIcon(icon2)
        self.btnBiblioteca.setIconSize(QSize(20, 20))

        self.layMenu_2.addWidget(self.btnBiblioteca)

        self.wdMenuPrincipal = QWidget(self.home)
        self.wdMenuPrincipal.setObjectName(u"wdMenuPrincipal")
        self.wdMenuPrincipal.setGeometry(QRect(0, 0, 400, 71))
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
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 361, 44))
        self.layMenuHome = QHBoxLayout(self.horizontalLayoutWidget)
        self.layMenuHome.setSpacing(2)
        self.layMenuHome.setObjectName(u"layMenuHome")
        self.layMenuHome.setContentsMargins(0, 0, 0, 0)
        self.btnConteudos = QPushButton(self.horizontalLayoutWidget)
        self.btnConteudos.setObjectName(u"btnConteudos")
        self.btnConteudos.setEnabled(True)
        icon3 = QIcon()
        icon3.addFile(u":/icons/conteudo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnConteudos.setIcon(icon3)
        self.btnConteudos.setIconSize(QSize(18, 18))

        self.layMenuHome.addWidget(self.btnConteudos)

        self.btnEmocoes = QPushButton(self.horizontalLayoutWidget)
        self.btnEmocoes.setObjectName(u"btnEmocoes")
        self.btnEmocoes.setStyleSheet(u"background-image: url(:/icones/notificacao.png) 10px 10px;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/emocoes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnEmocoes.setIcon(icon4)
        self.btnEmocoes.setIconSize(QSize(18, 18))

        self.layMenuHome.addWidget(self.btnEmocoes)

        self.btnLogout = QPushButton(self.horizontalLayoutWidget)
        self.btnLogout.setObjectName(u"btnLogout")
        icon5 = QIcon()
        icon5.addFile(u":/icons/login.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLogout.setIcon(icon5)
        self.btnLogout.setIconSize(QSize(18, 18))

        self.layMenuHome.addWidget(self.btnLogout)

        self.opcoes = QFrame(self.wdMenuPrincipal)
        self.opcoes.setObjectName(u"opcoes")
        self.opcoes.setGeometry(QRect(0, 40, 400, 31))
        self.opcoes.setFrameShape(QFrame.StyledPanel)
        self.opcoes.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget_2 = QWidget(self.opcoes)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(-10, -10, 381, 51))
        self.layOpcoes = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.layOpcoes.setSpacing(3)
        self.layOpcoes.setObjectName(u"layOpcoes")
        self.layOpcoes.setContentsMargins(0, 0, 0, 0)
        self.btnRaiva = QPushButton(self.horizontalLayoutWidget_2)
        self.btnRaiva.setObjectName(u"btnRaiva")
        icon6 = QIcon()
        icon6.addFile(u":/icons/raiva.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRaiva.setIcon(icon6)

        self.layOpcoes.addWidget(self.btnRaiva)

        self.btnOdio = QPushButton(self.horizontalLayoutWidget_2)
        self.btnOdio.setObjectName(u"btnOdio")

        self.layOpcoes.addWidget(self.btnOdio)

        self.btnTristeza = QPushButton(self.horizontalLayoutWidget_2)
        self.btnTristeza.setObjectName(u"btnTristeza")

        self.layOpcoes.addWidget(self.btnTristeza)

        self.opcoes_2 = QFrame(self.wdMenuPrincipal)
        self.opcoes_2.setObjectName(u"opcoes_2")
        self.opcoes_2.setGeometry(QRect(-20, 40, 400, 31))
        self.opcoes_2.setFrameShape(QFrame.StyledPanel)
        self.opcoes_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget_4 = QWidget(self.opcoes_2)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(20, -10, 361, 51))
        self.layOpcoes_2 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.layOpcoes_2.setSpacing(3)
        self.layOpcoes_2.setObjectName(u"layOpcoes_2")
        self.layOpcoes_2.setContentsMargins(0, 0, 0, 0)
        self.btnFilmes = QPushButton(self.horizontalLayoutWidget_4)
        self.btnFilmes.setObjectName(u"btnFilmes")

        self.layOpcoes_2.addWidget(self.btnFilmes)

        self.btnArtigos = QPushButton(self.horizontalLayoutWidget_4)
        self.btnArtigos.setObjectName(u"btnArtigos")

        self.layOpcoes_2.addWidget(self.btnArtigos)

        self.btnLivros = QPushButton(self.horizontalLayoutWidget_4)
        self.btnLivros.setObjectName(u"btnLivros")

        self.layOpcoes_2.addWidget(self.btnLivros)

        self.btnCanais = QPushButton(self.horizontalLayoutWidget_4)
        self.btnCanais.setObjectName(u"btnCanais")

        self.layOpcoes_2.addWidget(self.btnCanais)

        self.opcoes.raise_()
        self.horizontalLayoutWidget.raise_()
        self.opcoes_2.raise_()
        self.wdSidebar = QWidget(self.home)
        self.wdSidebar.setObjectName(u"wdSidebar")
        self.wdSidebar.setGeometry(QRect(310, 80, 41, 421))
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
        self.verticalLayoutWidget_8.setGeometry(QRect(0, 30, 41, 331))
        self.laySidebar = QVBoxLayout(self.verticalLayoutWidget_8)
        self.laySidebar.setObjectName(u"laySidebar")
        self.laySidebar.setContentsMargins(0, 0, 0, 0)
        self.btnNotifica = QPushButton(self.verticalLayoutWidget_8)
        self.btnNotifica.setObjectName(u"btnNotifica")
        self.btnNotifica.setMinimumSize(QSize(29, 32))
        self.btnNotifica.setMaximumSize(QSize(16777215, 32))
        self.btnNotifica.setStyleSheet(u"background-image: url(:/icones/notificacao.png) 10px 10px;")
        icon7 = QIcon()
        icon7.addFile(u":/icons/notificacao.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNotifica.setIcon(icon7)
        self.btnNotifica.setIconSize(QSize(20, 20))

        self.laySidebar.addWidget(self.btnNotifica)

        self.wdPesquisar = QWidget(self.home)
        self.wdPesquisar.setObjectName(u"wdPesquisar")
        self.wdPesquisar.setGeometry(QRect(0, 80, 301, 31))
        self.formLayoutWidget = QWidget(self.wdPesquisar)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 0, 291, 31))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.btnPesquisar = QPushButton(self.formLayoutWidget)
        self.btnPesquisar.setObjectName(u"btnPesquisar")
        self.btnPesquisar.setStyleSheet(u"*{\n"
"	background-color: rgb(30, 30, 30);\n"
"	border-radius: 7px;\n"
"	color: rgb(85, 255, 255)\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.btnPesquisar)

        self.lnPesquisar = QLineEdit(self.formLayoutWidget)
        self.lnPesquisar.setObjectName(u"lnPesquisar")
        self.lnPesquisar.setStyleSheet(u"*{\n"
"	background-color: rgb(30, 30, 30);\n"
"	border-radius: 7px;\n"
"	color: rgb(85, 255, 255);\n"
"	height: 18px;\n"
"	padding: 5px;\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lnPesquisar)

        self.login = QFrame(self.centralwidget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(0, 0, 360, 550))
        self.login.setMinimumSize(QSize(360, 550))
        self.login.setMaximumSize(QSize(360, 350))
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
        self.frLogo.setGeometry(QRect(-20, -50, 400, 500))
        self.frLogo.setStyleSheet(u"QFrame{\n"
"	image: url(:/logo/logo-cerebro.png);\n"
"}\n"
"")
        self.frLogo.setFrameShape(QFrame.StyledPanel)
        self.frLogo.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.login)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 370, 261, 131))
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

        DescomplicadaMente.setCentralWidget(self.centralwidget)
        self.login.raise_()
        self.home.raise_()
        QWidget.setTabOrder(self.sclaFeed, self.sclaConteudos)
        QWidget.setTabOrder(self.sclaConteudos, self.sclaNotificacao)
        QWidget.setTabOrder(self.sclaNotificacao, self.sclaBiblioteca)
        QWidget.setTabOrder(self.sclaBiblioteca, self.btnHome)
        QWidget.setTabOrder(self.btnHome, self.btnBiblioteca)
        QWidget.setTabOrder(self.btnBiblioteca, self.btnConteudos)
        QWidget.setTabOrder(self.btnConteudos, self.btnEmocoes)
        QWidget.setTabOrder(self.btnEmocoes, self.btnLogout)
        QWidget.setTabOrder(self.btnLogout, self.btnRaiva)
        QWidget.setTabOrder(self.btnRaiva, self.btnOdio)
        QWidget.setTabOrder(self.btnOdio, self.btnTristeza)
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
        self.btnOdio.setText(QCoreApplication.translate("DescomplicadaMente", u"Tristeza", None))
        self.btnTristeza.setText(QCoreApplication.translate("DescomplicadaMente", u"\u00d3dio", None))
        self.btnFilmes.setText(QCoreApplication.translate("DescomplicadaMente", u"Artigos", None))
        self.btnArtigos.setText(QCoreApplication.translate("DescomplicadaMente", u"Filmes", None))
        self.btnLivros.setText(QCoreApplication.translate("DescomplicadaMente", u"Livros", None))
        self.btnCanais.setText(QCoreApplication.translate("DescomplicadaMente", u"Canais", None))
        self.btnNotifica.setText("")
        self.btnPesquisar.setText(QCoreApplication.translate("DescomplicadaMente", u"Pesquisar", None))
        self.lnEmail.setPlaceholderText(QCoreApplication.translate("DescomplicadaMente", u"Email", None))
        self.lnSenha.setPlaceholderText(QCoreApplication.translate("DescomplicadaMente", u"Senha", None))
        self.btnEntrar.setText(QCoreApplication.translate("DescomplicadaMente", u"Entrar", None))
    # retranslateUi

