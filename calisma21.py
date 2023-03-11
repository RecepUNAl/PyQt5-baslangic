import sys
import PyQt5
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Merhaba Dünya")
        self.ad =QLabel("Ad")
        self.soyad =QLabel("Soyad")
        self.l1=QLineEdit()
        self.l2=QLineEdit()
        self.mail=QLabel("............")
        self.bt1=QPushButton("Oluştur.")

        v1=QVBoxLayout()
        h1=QHBoxLayout()
        h2=QHBoxLayout()

        h1.addWidget(self.ad)
        h1.addWidget(self.l1)

        h2.addWidget(self.soyad)
        h2.addWidget(self.l2)


        v1.addLayout(h1)
        v1.addLayout(h2)
        v1.addWidget(self.bt1)
        v1.addWidget(self.mail)

        self.bt1.clicked.connect(self.olustur)

        self.setLayout(v1)
        self.show()


    def olustur(self):
        a=self.l1.text()
        b=self.l2.text()
        c=(a[0]+b+"@gmail.com")
        self.mail.setText(c)
        
app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app