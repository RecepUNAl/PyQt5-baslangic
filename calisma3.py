import sys
import PyQt5
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Merhaba Dünya")
        self.etiket=QLabel("Bu bir deneme sayfasıdır ")
        self.ad=QLabel("Ad:")
        self.soyad=QLabel("Soyad:")
        self.bt1=QPushButton("Kaydet:")
        self.bt2=QPushButton("Sil:")
        
        v1=QVBoxLayout()
        h1=QHBoxLayout()
        h2=QHBoxLayout()
        
        h1.addWidget(self.ad)
        h1.addWidget(self.soyad)
        h1.addStretch()
        h2.addWidget(self.bt1)
        h2.addWidget(self.bt2)
        
        v1.addWidget(self.etiket)
        v1.addLayout(h1)
        v1.addStretch()
        v1.addLayout(h2)
        self.setLayout(v1)
        
        self.show()
        
app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app