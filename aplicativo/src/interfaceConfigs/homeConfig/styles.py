from PySide2 import QtWidgets

def alterarEstilo(ui):

    '''
        FUNÇÃO QUE ALTERA O CSS DE ACORDO COM A EMOÇÃO SELECIONADA
    '''

    def estilizarRaiva():
        # estilo = 
            
        ui.home.setStyleSheet('''
            QFrame {background: #2888ff;}
        ''')
        ui.horizontalLayoutWidget_5.setStyleSheet('''
            QPushButton {background-color: #2d2dee;}
        ''')
        # ui.wdConteudo.setStyleSheet('''
            # QPushButton{background-color: #2d2dee;}
        # ''')
        
    def estilizarTristeza():
        ui.home.setStyleSheet('''
            QFrame {background: #ff8828;}
        ''')
        ui.horizontalLayoutWidget_5.setStyleSheet('''
            QPushButton {background-color: #ffd222;}
        ''')
        # ui.wdConteudo.setStyleSheet('''
            # QPushButton{background-color: #2d2dee;}
        # ''')
    
    def estilizarDesespero():
        ui.home.setStyleSheet('''
            QFrame {background: #ffffff;}
        ''')
        ui.horizontalLayoutWidget_5.setStyleSheet('''
            QPushButton {background-color: #ffffff;}
        ''')
        # ui.wdConteudo.setStyleSheet('''
            # QPushButton{background-color: #2d2dee;}
        # ''')

    ui.btnRaiva.clicked.connect(estilizarRaiva)
    ui.btnTristeza.clicked.connect(estilizarTristeza)
    ui.btnDesespero.clicked.connect(estilizarDesespero)
