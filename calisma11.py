import sys
import PyQt5
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Merhaba")
        self.lnEdit    =QLineEdit()
        self.txtEdit   =QTextEdit()
        self.btnKaydet =QPushButton("Kaydet")
        self.btnSil    =QPushButton("Sil")

        h1=QHBoxLayout()
        h2=QHBoxLayout()
        h3=QHBoxLayout()
        v1=QVBoxLayout()

        h1.addWidget(self.lnEdit)

        h2.addWidget(self.txtEdit)

        h3.addWidget(self.btnKaydet)
        h3.addWidget(self.btnSil)

        v1.addLayout(h1)
        v1.addLayout(h2)
        v1.addLayout(h3)
        
        self.btnKaydet.clicked.connect(self.kaydet)
        self.btnSil.clicked.connect(self.sil)
        
        self.setLayout(v1)
        self.show()

    def kaydet(self):
        a=self.lnEdit.text()
        self.txtEdit.setText(a)
        self.lnEdit.clear()
        
    def sil(self):
        self.txtEdit.clear()

        
app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app