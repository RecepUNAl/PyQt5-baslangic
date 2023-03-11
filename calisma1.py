from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import time
import sys

class Pencere(QWidget):
    def _init_(self):
        super(Pencere, self)._init_()
        self.UI()
        self.r_top.setChecked(True)

    def UI(self):
        form = QFormLayout()
        h_box = QHBoxLayout()
        self.islem_yap_button = QPushButton("İşlemi Yap")
        self.islem_yap_button.clicked.connect(self.islem)
        self.sil_button = QPushButton("Temizle")
        self.sil_button.clicked.connect(self.temizle)
        qFont = QFont("Calibri",14,QFont.Bold)
        qIcon = QIcon("Logo_Haf.png")

        self.islem_Sonuc = QLabel()
        self.islem_Sonuc.setFont(qFont)

        self.s1_label = QLabel("Sayı1 : ")
        self.s2_label = QLabel("Sayı2 : ")

        self.s1_edit = QLineEdit()
        self.s2_edit = QLineEdit()

        self.r_top = QRadioButton("Topla")
        self.r_top.clicked.connect(self.islem)
        self.r_cikar = QRadioButton("Çıkar")
        self.r_cikar.clicked.connect(self.islem)
        self.r_carp = QRadioButton("Çarp")
        self.r_carp.clicked.connect(self.islem)
        self.r_bol = QRadioButton("Böl")
        self.r_bol.clicked.connect(self.islem)

        h_box.addWidget(self.r_top)
        h_box.addWidget(self.r_cikar)
        h_box.addWidget(self.r_carp)
        h_box.addWidget(self.r_bol)

        form.addRow(self.s1_label,self.s1_edit)
        form.addRow(self.s2_label,self.s2_edit)
        form.addRow(QLabel("İşlem : "),h_box)
        form.addRow(self.islem_yap_button)
        form.addRow(QLabel("İşlem Sonucu : "),self.islem_Sonuc)
        form.addRow(self.sil_button)

        self.setLayout(form)
        self.setGeometry(1000,400,400,180)
        self.setWindowTitle("Basit Hesap Makinesi")
        self.setWindowIcon(qIcon)
        self.show()

    def islem(self):
        try:
            if self.r_top.isChecked():
                self.islem_Sonuc.setText(str(float(self.s1_edit.text()) + float(self.s2_edit.text())))
            elif self.r_cikar.isChecked():
                self.islem_Sonuc.setText(str(float(self.s1_edit.text()) - float(self.s2_edit.text())))
            elif self.r_bol.isChecked():
                self.islem_Sonuc.setText(str(float(self.s1_edit.text()) / float(self.s2_edit.text())))
            elif self.r_carp.isChecked():
                self.islem_Sonuc.setText(str(float(self.s1_edit.text()) * float(self.s2_edit.text())))
            else:
                self.islem_Sonuc.setText("İşlem Seçimi Yapılmadı")
        except:
            self.islem_Sonuc.setText("HATA ! Girişleri Kontrol Ediniz !")

    def temizle(self):
        self.islem_Sonuc.setText("")
        self.s1_edit.setText("")
        self.s2_edit.setText("")
        self.s1_edit.setFocus()

app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app