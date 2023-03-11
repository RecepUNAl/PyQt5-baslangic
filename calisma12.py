import sys
import PyQt5
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Merhaba")
        self.soru     = QLabel("Soru")
        self.s_icerig = QLabel("Gönen ilçe nüfusu")
        self.a        =QRadioButton("80000")
        self.b        =QRadioButton("75000")
        self.c        =QRadioButton("70000")
        self.d        =QRadioButton("90000")

        h1=QHBoxLayout()
        h2=QHBoxLayout()
        h3=QHBoxLayout()
        h4=QHBoxLayout()
        h5=QHBoxLayout()
        v1=QVBoxLayout()

        h1.addWidget(self.soru)
        h1.addWidget(self.s_icerig)

        h2.addWidget(self.a)
        
        h3.addWidget(self.b)
        
        h4.addWidget(self.c)
        
        h5.addWidget(self.d)



        v1.addLayout(h1)
        v1.addStretch()
        v1.addLayout(h2)
        v1.addLayout(h3)
        v1.addLayout(h4)
        v1.addLayout(h5)

        self.setLayout(v1)
        self.show()

app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app