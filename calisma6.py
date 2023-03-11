import sys
import PyQt5
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.setWindowTitle("Hesap Makinesi")
        self.islem =QLineEdit()
        self.bir   =QPushButton("1")
        self.iki   =QPushButton("2")
        self.uc    =QPushButton("3")
        self.bol   =QPushButton("/")

        self.dort  =QPushButton("4")
        self.bes   =QPushButton("5")
        self.alti  =QPushButton("6")
        self.carp  =QPushButton("*")

        self.yedi  =QPushButton("7")
        self.sekiz =QPushButton("8")
        self.dokuz =QPushButton("9")
        self.topla =QPushButton("+")

        self.nokta =QPushButton(",")
        self.sifir =QPushButton("0")
        self.esit  =QPushButton("=")
        self.cikar =QPushButton("-")

        h1=QHBoxLayout()
        h2=QHBoxLayout()
        h3=QHBoxLayout()
        h4=QHBoxLayout()
        h5=QHBoxLayout()
        v1=QVBoxLayout()

        h1.addWidget(self.bir)
        h1.addWidget(self.iki)
        h1.addWidget(self.uc)
        h1.addWidget(self.bol)
        
        h2.addWidget(self.dort)
        h2.addWidget(self.bes)
        h2.addWidget(self.alti)
        h2.addWidget(self.carp)
        
        h3.addWidget(self.yedi)
        h3.addWidget(self.sekiz)
        h3.addWidget(self.dokuz)
        h3.addWidget(self.topla)

        h4.addWidget(self.nokta)
        h4.addWidget(self.sifir)
        h4.addWidget(self.esit)
        h4.addWidget(self.cikar)

        v1.addStretch()
        v1.addWidget(self.islem)
        v1.addLayout(h1)
        v1.addLayout(h2)
        v1.addLayout(h3)
        v1.addLayout(h4)
        v1.addStretch()

        h5.addStretch()
        h5.addLayout(v1)
        h5.addStretch()
        
        self.setLayout(h5)
        self.show()


app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app