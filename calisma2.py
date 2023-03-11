import sys
import PyQt5
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Merhaba Dünya")
        self.etiket=QLabel("Ad :")
        self.etiket2=QLabel("Soyad :")
        self.bt1=QPushButton("Tamam")
        self.bt2=QPushButton("Hayır")
        
        v1=QHBoxLayout()
        v1.addWidget(self.etiket)
        v1.addWidget(self.bt1)
        v1.addWidget(self.etiket2)
        v1.addWidget(self.bt2)
        self.setLayout(v1)
        
        self.show()
        
app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app