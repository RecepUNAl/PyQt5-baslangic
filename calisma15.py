import sys
import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class Pencere(QMainWindow):
    def _init_(self):
        super()._init_()
        self.init_ui()

    def init_ui(self):
        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")
        duzen = menubar.addMenu("Düzen")
        bicim = menubar.addMenu("Biçim")
        gorunum = menubar.addMenu("Görünüm")
        yardim = menubar.addMenu("Yardım")
        yakinlastir = gorunum.addMenu("Yakınlaştır")
        
        yeni = QAction("Yeni",self)
        yeni.setShortcut("Ctrl+N")
        yeni_pencere = QAction("Yeni Pencere",self)
        ac = QAction("Ac",self)
        kaydet = QAction("Kaydet",self)
        farkli_kaydet = QAction("Farklı Kaydet",self)
                
        geri_al = QAction("Geri Al",self)
        kes = QAction("Kes", self)
        kopyala = QAction("Kopyala", self)
        yapistir = QAction("Yapıstır", self)
        sil = QAction("Sil", self)
        
        sozcuk_kaydir = QAction("Sözcük Kaydır", self)
        yazi_tipi = QAction("Yazı Tipi...", self)
        
        durum_cubugu = QAction("Durum Çubuğu", self)
        
        yakinlastir2 = QAction("Yakınlaştır", self)
        uzaklastir = QAction("Uzaklaştır", self)
        varsayilan_yak = QAction("Varsayılan Yakınlaştırmayı Geri Yükle", self)
        
        grbildirm = QAction("Geri Bildirim Gönder",self)
        not_defter = QAction("Not Defteri Hakkında", self)
        
        dosya.addAction(yeni)
        dosya.addAction(yeni_pencere)
        dosya.addAction(ac)
        dosya.addAction(kaydet)
        dosya.addAction(farkli_kaydet)
        
        duzen.addAction(geri_al)
        duzen.addAction(kes)
        duzen.addAction(kopyala)
        duzen.addAction(yapistir)
        duzen.addAction(sil)
        
        bicim.addAction(sozcuk_kaydir)
        bicim.addAction(yazi_tipi)
        
        gorunum.addAction(durum_cubugu)
        
        yakinlastir.addAction(yakinlastir2)
        yakinlastir.addAction(uzaklastir)
        yakinlastir.addAction(varsayilan_yak)
        
        yardim.addAction(grbildirm)
        yardim.addAction(not_defter)
        
        self.show()

app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app