import sys
import PyQt5
from PyQt5.QtWidgets import *

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        menu=self.menuBar()
        kayit=menu.addMenu("Kayıt")
        arama=menu.addMenu("Arama")

        ogr1 = QAction("Öğrenci Ekle",self)
        ders1 = QAction("Ders Ekle",self)
        py = QAction("Python",self)
        grsl = QAction("Görsel",self)
        ogr2 = QAction("Öğrenci Ara",self)
        ders2 = QAction("Ders Ara",self)

        kayit.addAction(ogr1)

        dersmenu=kayit.addMenu("Ders Ekle")

        arama.addAction(ogr2)
        arama.addAction(ogr2)
        dersmenu.addAction(py)
        dersmenu.addAction(grsl)

        self.show()

app=QApplication(sys.argv)
pencere=Pencere()
app.exec_()
del app