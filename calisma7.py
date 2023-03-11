import sys
from unicodedata import name
import PyQt5
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.setWindowTitle("Hesap Makinesi")
        self.islem =QLineEdit()
        g1 = QGridLayout()

        v1=QVBoxLayout()
        
        liste=[1,2,3,"/",4,5,6,"x",7,8,9,"+",".",0,"=","-",]
        y=0
        x=0
        for nm in liste:
            name = str(nm)
            button = QPushButton(name)
            g1.addWidget(button,y,x)
            y=y+1
            x=x+1
        v1.addWidget(self.line)
        v1.addLayout(g1)

        self.setLayout(v1)
        self.show()


app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app