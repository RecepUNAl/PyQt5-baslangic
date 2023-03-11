import sys
import PyQt5
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Merhaba Dünya")
        self.s1 = QLabel("Sayı 1")
        self.s2 = QLabel("Sayı 2")
        self.s1_edit = QLineEdit()
        self.s2_edit = QLineEdit()
        self.topla = QPushButton("+")
        self.cikar = QPushButton("-")
        self.carp = QPushButton("*")
        self.bol = QPushButton("/")
        self.temizle = QPushButton("Temizle")
        self.sonuc = QLabel("............")

        h1=QHBoxLayout()
        h2=QHBoxLayout()
        h3=QHBoxLayout()
        h4=QHBoxLayout()
        h5=QHBoxLayout()
        v1=QVBoxLayout()

        h1.addWidget(self.s1)
        h1.addWidget(self.s1_edit)

        h2.addWidget(self.s2)
        h2.addWidget(self.s2_edit)

        h3.addWidget(self.topla)
        h3.addWidget(self.cikar)
        h3.addWidget(self.carp)
        h3.addWidget(self.bol)

        h4.addWidget(self.sonuc)

        h5.addWidget(self.temizle)


        v1.addLayout(h1)
        v1.addLayout(h2)
        v1.addLayout(h3)
        v1.addLayout(h4)
        v1.addLayout(h5)

        self.setLayout(v1)
        self.show()


        self.carp.clicked.connect(self.islem)
        self.bol.clicked.connect(self.islem)
        self.topla.clicked.connect(self.islem)
        self.cikar.clicked.connect(self.islem)

        self.temizle.clicked.connect(self.temizlee)




    def islem(self):
        if self.sender() == self.topla:
            self.sonuc.setText(str(float(self.s1_edit.text()) + float(self.s2_edit.text())))

        elif self.sender() == self.cikar:
            self.sonuc.setText(str(float(self.s1_edit.text()) - float(self.s2_edit.text())))

        elif self.sender() == self.carp:
            self.sonuc.setText(str(float(self.s1_edit.text()) * float(self.s2_edit.text())))

        elif self.sender() == self.bol:
            self.sonuc.setText(str(float(self.s1_edit.text()) / float(self.s2_edit.text())))

    def temizlee(self):
        self.sonuc.setText("")
        self.s2_edit.setText("")
        self.s1_edit.setText("")



app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app