import sys
import PyQt5
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Form")
        self.ad     =QLabel("Adı")
        self.soyad  =QLabel("Soyadı")
        self.vize   =QLabel("Vize")
        self.final  =QLabel("Final")
        self.line1  =QLineEdit()
        self.line2  =QLineEdit()
        self.line3  =QLineEdit()
        self.line4  =QLineEdit()
        self.mesaj  =QLabel("Öğrenci Kayıt Sayfası")
        self.btn1   =QPushButton("Listele")
        self.btn2   =QPushButton("Kaydet")

        h1=QHBoxLayout()
        h2=QHBoxLayout()
        h3=QHBoxLayout()
        h4=QHBoxLayout()
        v1=QVBoxLayout()

        h1.addWidget(self.ad)
        h1.addStretch()
        h1.addWidget(self.line1)
        
        h2.addWidget(self.soyad)
        h2.addStretch()
        h2.addWidget(self.line2)

        h3.addWidget(self.vize)
        h3.addWidget(self.line3)
        h3.addWidget(self.final)
        h3.addWidget(self.line4)

        v1.addStretch()
        v1.addLayout(h1) 
        v1.addLayout(h2)
        v1.addWidget(self.btn1)
        v1.addLayout(h3)
        v1.addWidget(self.btn2)
        v1.addStretch()

        h4.addStretch()
        h4.addLayout(v1)
        h4.addStretch()


        self.setLayout(h4)
        self.show()

app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app