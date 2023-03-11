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
        self.lab   =QLabel("Labaratuvar:")
        self.txtLab=QLineEdit()
        self.ders  =QLabel("Ders")
        self.devam =QLabel("Devam")
        self.rdoBtnNesne=QRadioButton("Nesne 1")
        self.rdoBtnRobotik=QRadioButton("Robotik 1")
        self.rdoBtnDigital=QRadioButton("Dijital")
        self.rdoBtnAlgoritma=QRadioButton("Algoritma")
        self.txtZorunlu  =QCheckBox("Zorunlu")
        self.txtOnline   =QCheckBox("Online")

        h1=QHBoxLayout()
        h2=QHBoxLayout()
        v1=QVBoxLayout()
        v2=QVBoxLayout()
        v3=QVBoxLayout()

        h1.addWidget(self.lab)
        h1.addWidget(self.txtLab)

        v1.addStretch()
        v1.addWidget(self.ders)
        v1.addWidget(self.rdoBtnNesne)
        v1.addWidget(self.rdoBtnRobotik)
        v1.addWidget(self.rdoBtnDigital)
        v1.addWidget(self.rdoBtnAlgoritma)

        v2.addStretch()
        v2.addWidget(self.devam)
        v2.addWidget(self.txtZorunlu)
        v2.addWidget(self.txtOnline)

        h2.addLayout(v1)
        h2.addStretch()
        h2.addLayout(v2)

        v3.addLayout(h1)
        v3.addLayout(h2)

        self.setLayout(v3)
        self.show()

app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app