from cProfile import label
import sys
from tkinter import Widget
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
        self.line1  =QLineEdit()
        self.line2  =QLineEdit()
        self.mesaj  =QLabel("Öğrenci Kayıt Sayfası")
        self.bt1    =QPushButton("Kaydet")
        self.bt2    =QPushButton("Sil")

        h1=QHBoxLayout()
        h2=QHBoxLayout()
        v1=QVBoxLayout()

        h1.addWidget(self.ad)
        h1.addWidget(self.line1)
        h1.addWidget(self.soyad)
        h1.addWidget(self.line2)

        h2.addWidget(self.bt1)
        h2.addStretch()
        h2.addWidget(self.bt2)

        v1.addLayout(h1)
        v1.addWidget(self.mesaj)
        v1.addStretch()
        v1.addLayout(h2)

        self.setLayout(v1)

        self.show()

app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app












