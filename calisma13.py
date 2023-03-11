import sys
import PyQt5
from PyQt5.QtWidgets import *

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Cevap Anahtarı")
        bos = QLabel("")
        a = QLabel("A")
        b = QLabel("B")
        c = QLabel("C")
        d = QLabel("D")
        e = QLabel("E")

        h1=QHBoxLayout()
        v1=QVBoxLayout()

        h1.addWidget(bos)
        h1.addWidget(a)
        h1.addWidget(b)
        h1.addWidget(c)
        h1.addWidget(d)
        v1.addLayout(h1)

        for i in range(1,21):
            lbl=QLabel(str(i))
            h=QHBoxLayout()
            h.addWidget(lbl)
            for x in range(5):
                btn=QRadioButton()
                h.addWidget(btn)
            v1.addLayout(h)        

        self.setLayout(v1)
        self.show()

app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app