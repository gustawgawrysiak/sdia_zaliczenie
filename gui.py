import os
import shutil
from json import JSONDecodeError

from PyQt5 import QtCore
from PyQt5.QtWidgets import (
QApplication,
QMainWindow,
QWidget,
QGridLayout,
QCheckBox,
QRadioButton,
QFileDialog,
QPushButton,
QLabel,
QLineEdit
)
from warehouse import *
from parcels_export import ParcelsExport
# from PyQt5.QtGui import *

class MyWindow(QMainWindow):

    def __init__(self, window_name):
        super().__init__()

        """ustawienie minimalnych wymiarów okna dialogowego
        oraz tytułu okna"""

        self.setMinimumHeight(30)
        self.setMinimumWidth(380)

        self.window_title(window_name)
        container = QWidget()
        self.setCentralWidget(container)

        """utworzenie layoutu oraz umieszczenie w nim
        wszystkich przycisków, linii edycji oraz etykiet"""

        self.layout = QGridLayout()

        lbl_parcels = QLabel('Aby rozpocząć pracę z programem wybierz 2 pliki .json z paczkami i ciężarówkami')
        lbl_parcels.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(lbl_parcels, 0, 0)

        btn_load_parcels = QPushButton('Wczytaj plik z paczkami')
        self.layout.addWidget(btn_load_parcels, 2, 0, 2, 0)
        btn_load_parcels.clicked.connect(self.load_parcels_json)

        btn_load_trucks = QPushButton('Wczytaj plik z ciężarówkami')
        self.layout.addWidget(btn_load_trucks, 4, 0, 2, 0)
        btn_load_trucks.clicked.connect(self.load_trucks_json)

        container.setLayout(self.layout)

    def window_title(self, tytul):
        self.setWindowTitle(tytul)

    def load_parcels_json(self):
        self.file = QFileDialog.getOpenFileName(self, 'Wskaż plik json', '', 'Wszystkie pliki (*.*);; Plik json (*.json)', 'Plik json (*.json)')
        try:
            parcels = ParcelsImport.import_json(self.file[0])
            return parcels
        except JSONDecodeError:
            lbl_json = QLabel('Wskazano plik o formacie innym niż json. Proszę spróbować ponownie.')
            lbl_json.setAlignment(QtCore.Qt.AlignCenter)
            self.layout.addWidget(lbl_json, 1, 0)
        except FileNotFoundError:
            pass

    def load_trucks_json(self):
        self.file = QFileDialog.getOpenFileName(self, 'Wskaż plik json', '', 'Wszystkie pliki (*.*);; Plik json (*.json)', 'Plik json (*.json)')
        try:
            if ParcelsExport.import_json(self.file[0]) and self.load_parcels_json:
                # uruchomienie sryptu
                self.layout.addWidget(QLabel(str(self.load_parcels_json)))
        except JSONDecodeError:
            lbl_json = QLabel('Wskazano plik o formacie innym niż json. Proszę spróbować ponownie.')
            lbl_json.setAlignment(QtCore.Qt.AlignCenter)
            self.layout.addWidget(lbl_json, 1, 0)
        except FileNotFoundError:
            pass

    def script(self, parcels=None, trucks=None):
        # raise NotImplementedError
        pass




if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow('Magazyn przerzutowy')
    window.show()
    app.exec()