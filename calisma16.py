import sys
import PyQt5
from PyQt5.QtWidgets import *
class Pencere(QWidget):
    def _init_(self):
        super()._init_()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Hesap Makinesi")
        self.line=QLineEdit()
        liste=[1,2,3,"/",4,5,6,"x",7,8,9,"+",".",0,"=","-"]
        
        v1=QVBoxLayout()
        h1=QHBoxLayout()
        h2=QHBoxLayout()
        h3=QHBoxLayout()
        h4=QHBoxLayout()
        
        for x,i in enumerate(liste):
            button = QPushButton(str(i))
            if(x<4):
                h1.addWidget(button)  
            elif(x<8):
                h2.addWidget(button)
            elif(x<12):
                h3.addWidget(button)
            else:
                h4.addWidget(button)
        v1.addWidget(self.line)
        v1.addLayout(h1)
        v1.addLayout(h2)
        v1.addLayout(h3)
        v1.addLayout(h4)
        self.setLayout(v1)        
        self.show()
        
app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app