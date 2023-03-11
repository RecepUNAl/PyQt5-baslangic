from cProfile import label
import sys
import PyQt5
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Form")
        self.ad       =QLabel("Adı")
        self.soyad    =QLabel("Soyadı")
        self.ogr1     =QLabel("1.Öğretim")
        self.ogr2     =QLabel("2.Öğretim")
        self.txtAd    =QLineEdit()
        self.txtSoyad =QLineEdit()
        self.txtOgr1  =QCheckBox()
        self.txtOgr2  =QCheckBox()
        self.txtEdit  =QTextEdit()
        
        h1=QHBoxLayout()
        h2=QHBoxLayout()
        h3=QHBoxLayout()
        h4=QHBoxLayout()
        h5=QHBoxLayout()
        h6=QHBoxLayout()
        h7=QHBoxLayout()
        v1=QVBoxLayout()

        h1.addWidget(self.ad)
        h1.addWidget(self.txtAd)

        h2.addWidget(self.soyad)
        h2.addWidget(self.txtSoyad)

        h3.addLayout(h1)
        h3.addStretch()
        h3.addLayout(h2)

        h4.addWidget(self.ogr1)
        h4.addWidget(self.txtOgr1)

        
        h5.addWidget(self.ogr2)
        h5.addWidget(self.txtOgr2)

        h6.addWidget(self.txtEdit)

        v1.addStretch()
        v1.addLayout(h3)
        v1.addLayout(h4)
        v1.addLayout(h5)
        v1.addLayout(h6)
        v1.addStretch()

        h7.addStretch()
        h7.addLayout(v1)
        h7.addStretch()
        

        self.setLayout(h7)
        self.show()

app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app