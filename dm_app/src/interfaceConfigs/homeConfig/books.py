from PySide2.QtCore import ( QRect )
from models.modelBooks import ( getBooks )
from PySide2.QtWidgets import *

def configBooks(ui):

    def contentConfig(compName, listName, tableColumn):
        compName.setText(f'<font color=white align=center>{tableColumn}</font>')
        listName.append(compName)

    ui.groupBox = QGroupBox('<font color=white>Teste</font>')

    moviesList = getMovies()

    if moviesList:
        listaTitulo = list()
        listaSinopse = list()
        listaBotao = list()

        for i, f in enumerate(moviesList):
            ui.lbTitulo = QLabel(ui.verticalLayoutWidget_7)
            contentConfig(ui.lbTitulo, listaTitulo, f[1])
            
            ui.lbSinopse = QLabel(ui.verticalLayoutWidget_7)
            contentConfig(ui.lbSinopse, listaSinopse, f[2])
            
            ui.btnAdicionar = QPushButton(ui.verticalLayoutWidget_7)
            ui.btnAdicionar.setStyleSheet('background-color: #00ffff;')
            ui.btnAdicionar.setText('Adicionar')
            listaBotao.append(ui.btnAdicionar)

            ui.layConteudo_2.addWidget(listaTitulo[i])
            ui.layConteudo_2.addWidget(listaSinopse[i])
            ui.layConteudo_2.addWidget(listaBotao[i])

        ui.groupBox.setLayout(ui.layConteudo_2)
        ui.sclaConteudos.setWidget(ui.groupBox)
        ui.sclaConteudos.setFixedHeight(380)