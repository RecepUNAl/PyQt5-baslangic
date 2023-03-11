import sys

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):


        h1 = QHBoxLayout()
        h2 = QHBoxLayout()
        h3 = QHBoxLayout()
        v1 = QVBoxLayout()

        self.yazi = ""
        self.adlbl = QLabel("A")
        self.soyadlbl = QLabel("B")
        self.txtAd = QLineEdit()
        self.txtSoyad = QLineEdit()
        self.txtKaydet = QLabel("---")
        self.btnarti = QPushButton("+")
        self.btneksi = QPushButton("-")
        self.btncarpi = QPushButton("*")
        self.btnbolu = QPushButton("/")





        h1.addWidget(self.adlbl)
        h1.addWidget(self.txtAd)

        h2.addWidget(self.soyadlbl)
        h2.addWidget(self.txtSoyad)

        h3.addWidget(self.btnarti)
        h3.addWidget(self.btneksi)
        h3.addWidget(self.btncarpi)
        h3.addWidget(self.btnbolu)

        v1.addLayout(h1)
        v1.addLayout(h2)
        v1.addLayout(h3)
        v1.addWidget(self.txtKaydet)

        self.btnarti.clicked.connect(self.kaydetBtn)
        self.btneksi.clicked.connect(self.kaydetBtn)
        self.btncarpi.clicked.connect(self.kaydetBtn)
        self.btnbolu.clicked.connect(self.kaydetBtn)

        self.setLayout(v1)

    def kaydetBtn(self):
        if self.sender() == self.btnarti:
            topla = int(self.txtAd.text()) + int(self.txtSoyad.text())
            self.txtKaydet.setText(str(topla))

        elif self.sender() == self.btneksi:
            eksi = int(self.txtAd.text()) - int(self.txtSoyad.text())
            self.txtKaydet.setText(str(eksi))

        elif self.sender() == self.btncarpi:
            carp = int(self.txtAd.text()) * int(self.txtSoyad.text())
            self.txtKaydet.setText(str(carp))

        elif self.sender() == self.btnbolu:
            bol = int(self.txtAd.text()) / int(self.txtSoyad.text())
            self.txtKaydet.setText(str(bol))

app = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
app.exec()
del app