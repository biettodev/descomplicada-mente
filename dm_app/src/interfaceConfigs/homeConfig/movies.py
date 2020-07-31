from PySide2.QtCore import ( QRect, QSize )
from models.modelMovies import ( getMovies )
from PySide2.QtWidgets import *

'''
    CONFIGURAÇÃO DO QUADRO DE CONTEÚDOS
'''

def configMovies(ui):

    def contentConfig(compName, listName, tableColumn):
        compName.setText(f'<font color=white align=center>{tableColumn}</font>')
        # compName
        listName.append(compName)

    ui.groupBox = QGroupBox('<font color=white>Teste</font>')

    moviesList = getMovies()

    if moviesList:
        
        # Criação das listas de cada elemento
        listaTitulo = list()
        listaSinopse = list()
        listaAutor = list()
        listaLikes = list()
        listaBotao = list()

        for i, f in enumerate(moviesList):
        
            # Configura a legenda de título
            ui.lbTitulo = QLabel(ui.verticalLayoutWidget_7)
            contentConfig(ui.lbTitulo, listaTitulo, f[1])
            
            
            # Configura a legenda de sinópse
            ui.lbSinopse = QLabel(ui.verticalLayoutWidget_7)
            ui.lbSinopse.setMaximumSize(QSize(380, 300))
            ui.lbSinopse.setMinimumSize(QSize(380, 50))
            ui.lbSinopse.setWordWrap(True)
            contentConfig(ui.lbSinopse, listaSinopse, f[2])
            
            # Configura a legenda com nome do autor
            ui.lbAutor = QLabel(ui.verticalLayoutWidget_7)
            contentConfig(ui.lbAutor, listaAutor, f[3])
            
            # Configura a legenda com quantidade de curtidas do conteúdo
            ui.lbLikes = QLabel(ui.verticalLayoutWidget_7)
            ui.lbLikes.setText(f'<font color=white align=center>{f[4]} gostaram disto!</font>')
            listaLikes.append(ui.lbLikes)
            
            # Configura o botão de adicionar
            ui.btnAdicionar = QPushButton(ui.verticalLayoutWidget_7)
            ui.btnAdicionar.setStyleSheet('background-color: #00ffff;')
            ui.btnAdicionar.setText('Adicionar')
            listaBotao.append(ui.btnAdicionar)

            ui.layConteudo_2.addWidget(listaTitulo[i])
            ui.layConteudo_2.addWidget(listaSinopse[i])
            ui.layConteudo_2.addWidget(listaAutor[i])
            ui.layConteudo_2.addWidget(listaLikes[i])
            ui.layConteudo_2.addWidget(listaBotao[i])

        ui.groupBox.setLayout(ui.layConteudo_2)
        ui.sclaConteudos.setWidget(ui.groupBox)
        ui.sclaConteudos.setFixedHeight(380)
