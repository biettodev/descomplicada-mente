from PySide2 import QtWidgets
from models.movies import getMovies
from models.channels import getChannels

'''
    CONFIGURAÇÃO DO QUADRO DE CONTEÚDOS
'''

def configConteudos(ui):

    def contentConfig(compName, listName, tableColumn):
        compName.setText(f'<font color=white align=center>{f[tableColumn]}</font>')
        listName.append(compName)

    ui.groupBox = QtWidgets.QGroupBox('<font color=white>Teste</font>')

    moviesList = getMovies()
    channelsList = getChannels()

    if moviesList:
        listaTitulo = list()
        listaSinopse = list()
        listaBotao = list()

        for i, f in enumerate(moviesList):
            ui.lbTitulo = QtWidgets.QLabel(ui.verticalLayoutWidget_7)
            contentConfig(ui.lbTitulo, listaTitulo, 1)
            
            ui.lbSinopse = QtWidgets.QLabel(ui.verticalLayoutWidget_7)
            contentConfig(ui.lbSinopse, listaSinopse, 2)
            
            ui.btnAdicionar = QtWidgets.QPushButton(ui.verticalLayoutWidget_7)
            ui.btnAdicionar.setStyleSheet('background-color: #00ffff;')
            ui.btnAdicionar.setText('Adicionar')
            listaBotao.append(ui.btnAdicionar)

            ui.layConteudo_2.addWidget(listaTitulo[i])
            ui.layConteudo_2.addWidget(listaSinopse[i])
            ui.layConteudo_2.addWidget(listaBotao[i])
        print('Quadro Conteúdos configurado')

        ui.groupBox.setLayout(ui.layConteudo_2)
        ui.sclaConteudos.setWidget(ui.groupBox)
        ui.sclaConteudos.setFixedHeight(300)
