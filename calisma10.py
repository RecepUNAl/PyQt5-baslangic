import sys
import PyQt5
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Form")
        self.sayi=0
        self.lbl     =QLabel("0")
        self.num     =QLCDNumber()
        self.btnArti =QPushButton("+")
        self.btnEksi =QPushButton("-")
        self.num.display("0")

        h1=QHBoxLayout()
        h2=QHBoxLayout()
        v1=QVBoxLayout()

        h1.addStretch()
        h1.addWidget(self.num)
        h1.addStretch()

        h2.addWidget(self.btnArti)
        h2.addWidget(self.btnEksi)

        v1.addLayout(h1)
        v1.addLayout(h2)

        self.btnArti.clicked.connect(self.art)
        self.btnEksi.clicked.connect(self.azal)
        self.setLayout(v1)
        self.show()

    def art(self):
        self.sayi+=1
        self.num.display(str(self.sayi))

    def azal(self):
        self.sayi-=1
        self.num.display(str(self.sayi))

        

app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app