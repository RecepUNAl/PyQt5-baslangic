import sys
import PyQt5
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Merhaba Dünya")
        self.a=QLabel("A")
        self.b =QLabel("B")
        self.l1=QLineEdit()
        self.l2=QLineEdit()
        self.sonuc=QLabel("............")
        self.btarti=QPushButton("+")
        self.bteksi=QPushButton("-")
        self.btcarp=QPushButton("*")
        self.btbol=QPushButton("/")

        v1=QVBoxLayout()
        h1=QHBoxLayout()
        h2=QHBoxLayout()
        h3=QHBoxLayout()

        h1.addWidget(self.a)
        h1.addWidget(self.l1)
        h2.addWidget(self.b)
        h2.addWidget(self.l2)
        h3.addWidget(self.btarti)
        h3.addWidget(self.bteksi)
        h3.addWidget(self.btcarp)
        h3.addWidget(self.btbol)


        v1.addLayout(h1)
        v1.addLayout(h2)
        v1.addLayout(h3)
        v1.addWidget(self.sonuc)

        self.btarti.clicked.connect(self.topla)
        self.bteksi.clicked.connect(self.cikar)
        self.btcarp.clicked.connect(self.carp)
        self.btbol.clicked.connect(self.bol)

        self.setLayout(v1)
        self.show()


    def topla(self):
        a=self.l1.text()
        b=self.l2.text()
        c=(a+b)
        self.sonuc.setText(c)

    def cikar(self):
        a=self.l1.text()
        b=self.l2.text()
        c=(a+b)
        self.sonuc.setText(c)

    def carp(self):
        a=self.l1.text()
        b=self.l2.text()
        c=(a+b)
        self.sonuc.setText(c)

    def bol(self):
        a=self.l1.text()
        b=self.l2.text()
        c=(a+b)
        self.sonuc.setText(c)    
        
app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app