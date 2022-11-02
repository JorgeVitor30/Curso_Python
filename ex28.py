import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, \
    QGridLayout

class App(QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.cw = QWidget() # CENTRAL WIDGET
        self.grid = QGridLayout(self.cw) # GRID
        
        self.btn = QPushButton('Texto Do botão')  # BUTTOM
        self.btn.setStyleSheet('font-size:25px;')
        
        # linha , coluna , qtd de lihas ocupar, qnts colunas ocupar
        self.grid.addWidget(self.btn,0,0, 1, 1)

        self.btn.clicked.connect(self.acao)
    
        self.setCentralWidget(self.cw)


    def acao(self):
        print('TESTE')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
    
    
