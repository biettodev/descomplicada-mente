from PySide2 import QtWidgets

def alterarEstilo(ui):

    '''
        FUNÇÃO QUE ALTERA O CSS DE ACORDO COM A EMOÇÃO SELECIONADA
    '''

    def estilizarRaiva():
    
        # Azul mais escuro - 1265a8
        # Azul mais fraco - 2888ff
        # Azul intermediário - 33bafe
        
        backgroundS1 = '''
            QFrame{
                background-color: #1265a8;;
                border-radius: 6px;
            }
            QPushButton{
                background-color: #33bafe; 
                text-transform: uppercase;
                border-radius: 6px;
            }
            '''
        
        backgroundS2 = '''
            QFrame{
                background-color: #1265a8;
                border-radius: 6px;
            }
            QPushButton{
                background-color: #2888ff; 
                text-transform: uppercase;
                border-radius: 6px;
            }
        '''
        
        buttonS1 = '''
            background-color: #2888ff; 
            text-transform: uppercase;
            border-radius: 6px;
            QPushButton{
                background-color: #33bafe; 
                text-transform: uppercase;
            }
            '''
        
        buttonS2 = '''
            QFrame{
                background-color: #1265a8;
                border-radius: 6px;
            }
            QPushButton{
                background-color: #33bafe; 
                text-transform: uppercase;
                border-radius: 6px;
            }
            '''
        
        ui.home.setStyleSheet(backgroundS2)
        
        ui.horizontalLayoutWidget.setStyleSheet(backgroundS1)
        
        ui.horizontalLayoutWidget_2.setStyleSheet(buttonS1)
        
        ui.horizontalLayoutWidget_4.setStyleSheet(buttonS1)
        
        ui.horizontalLayoutWidget_5.setStyleSheet(backgroundS1) 
        
        ui.wdSidebar.setStyleSheet(buttonS1)
        
        ui.wdPesquisar.setStyleSheet(backgroundS1)
        
        ui.btnChat.setStyleSheet(buttonS2)
        
        ui.btnNotifica.setStyleSheet(buttonS2)
        
        ui.btnPesquisar.setStyleSheet(buttonS1)
        
        ui.lnPesquisar.setStyleSheet(buttonS1)
        
    def estilizarTristeza():
    
        # Laranja mais intenso - ff8828
        # Amarelo - efd222
        # Laranja opaco - ddba4f
        
        backgroundS1 = '''
            QFrame{
                background-color: #ff8828;;
                border-radius: 6px;
            }
            QPushButton{
                background-color: #efd222; 
                text-transform: uppercase;
                border-radius: 6px;
            }
            '''
        
        backgroundS2 = '''
            QFrame{
                background-color: #ff8828;
                border-radius: 6px;
            }
            QPushButton{
                background-color: #ddba4f; 
                text-transform: uppercase;
                border-radius: 6px;
            }
        '''
        
        buttonS1 = '''
            background-color: #ddba4f; 
            text-transform: uppercase;
            border-radius: 6px;
            QPushButton{
                background-color: #efd222; 
                text-transform: uppercase;
            }
            '''
        
        buttonS2 = '''
            QFrame{
                background-color: #ff8828;
                border-radius: 6px;
            }
            QPushButton{
                background-color: #efd222; 
                text-transform: uppercase;
                border-radius: 6px;
            }
            '''
        
        ui.home.setStyleSheet(backgroundS2)
        
        ui.horizontalLayoutWidget.setStyleSheet(backgroundS1)
        
        ui.horizontalLayoutWidget_2.setStyleSheet(buttonS1)
        
        ui.horizontalLayoutWidget_4.setStyleSheet(buttonS1)
        
        ui.horizontalLayoutWidget_5.setStyleSheet(backgroundS1) 
        
        ui.wdSidebar.setStyleSheet(buttonS1)
        
        ui.btnChat.setStyleSheet(buttonS2)
        
        ui.btnNotifica.setStyleSheet(buttonS2)
        
        ui.wdPesquisar.setStyleSheet(backgroundS1)
        
        ui.btnPesquisar.setStyleSheet(buttonS1)
        
        ui.lnPesquisar.setStyleSheet(buttonS1)
    
    def estilizarDesespero():
        # Branco - cfcfcf
        # Cinza rosado - ababab
        # Roxo - a8a7a9
        
        backgroundS1 = '''
            QFrame{
                background-color: #cfcfcf;;
                border-radius: 6px;
            }
            QPushButton{
                background-color: #ababab; 
                text-transform: uppercase;
                border-radius: 6px;
            }
            '''
        
        backgroundS2 = '''
            QFrame{
                background-color: #cfcfcf;
                border-radius: 6px;
            }
            QPushButton{
                background-color: #a8a7a9; 
                text-transform: uppercase;
                border-radius: 6px;
            }
        '''
        
        backgroundS3 = '''
            background-color: #ababab; 
            text-transform: uppercase;
            border-radius: 6px;
            color: white;
        '''
        
        buttonS1 = '''
            background-color: #774488; 
            text-transform: uppercase;
            border-radius: 6px;
            color: white;
            QPushButton{
                background-color: #ababab; 
                text-transform: uppercase;
            }
            '''
        
        buttonS2 = '''
            QFrame{
                background-color: #ababab;
                border-radius: 6px;
            }
            QPushButton{
                background-color: #ababab; 
                text-transform: uppercase;
                border-radius: 6px;
            }
            '''
            
        ui.scrollAreaWidgetContents_2.setStyleSheet(buttonS1)
        
        ui.home.setStyleSheet(backgroundS2)
        
        ui.horizontalLayoutWidget.setStyleSheet(backgroundS1)
        
        ui.horizontalLayoutWidget_2.setStyleSheet(buttonS1)
        
        ui.horizontalLayoutWidget_4.setStyleSheet(buttonS1)
        
        ui.horizontalLayoutWidget_5.setStyleSheet(buttonS2) 
        
        ui.wdSidebar.setStyleSheet(backgroundS3)
        
        ui.btnChat.setStyleSheet(buttonS1)
        
        ui.btnNotifica.setStyleSheet(buttonS1)
        
        ui.wdPesquisar.setStyleSheet(backgroundS1)
        
        ui.btnPesquisar.setStyleSheet(buttonS1)
        
        ui.lnPesquisar.setStyleSheet(buttonS1)        

    ui.btnRaiva.clicked.connect(estilizarRaiva)
    ui.btnTristeza.clicked.connect(estilizarTristeza)
    ui.btnDesespero.clicked.connect(estilizarDesespero)
