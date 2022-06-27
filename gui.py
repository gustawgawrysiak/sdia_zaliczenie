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
QLineEdit,
QButtonGroup,
QMessageBox
)
from functools import partial
from warehouse import *
from parcels_export import ParcelsExport
# from PyQt5.QtGui import *

class MyWindow(QMainWindow):

    def __init__(self, window_name):
        super().__init__()

        """ustawienie minimalnych wymiarów okna dialogowego
        oraz tytułu okna"""

        self.setMinimumHeight(150)
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

        self.btn_load_parcels = QPushButton('Wczytaj plik z paczkami')
        self.layout.addWidget(self.btn_load_parcels, 4, 0, 2, 0)
        self.btn_load_parcels.clicked.connect(self.load_parcels_json)

        self.btn_load_trucks = QPushButton('Wczytaj plik z ciężarówkami')
        self.layout.addWidget(self.btn_load_trucks, 6, 0, 2, 0)
        self.btn_load_trucks.clicked.connect(self.load_trucks_json)

        container.setLayout(self.layout)

    def window_title(self, tytul):
        self.setWindowTitle(tytul)

    def load_parcels_json(self):
        file = QFileDialog.getOpenFileName(self, 'Wskaż plik json', '', 'Wszystkie pliki (*.*);; Plik json (*.json)', 'Plik json (*.json)')
        try:
            path = os.path.normpath(file[0])
            self.file_parcels = path.split(os.sep)[-1]
            ParcelsImport.import_json(self.file_parcels)
            if self.file_parcels and self.file_trucks:
                self.check_json_structure()
        except JSONDecodeError:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText('Wskazano plik o formacie innym niż json. Proszę spróbować ponownie.')
            msgBox.setWindowTitle('Warning')
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        except FileNotFoundError:
            pass
        except:
            pass

    def load_trucks_json(self):
        file = QFileDialog.getOpenFileName(self, 'Wskaż plik json', '', 'Wszystkie pliki (*.*);; Plik json (*.json)', 'Plik json (*.json)')
        try:
            path = os.path.normpath(file[0])
            self.file_trucks = path.split(os.sep)[-1]
            ParcelsExport.import_json(self.file_trucks)
            if self.file_trucks and self.file_parcels:
                self.check_json_structure()
        except JSONDecodeError:
            lbl_json = QLabel('Wskazano plik o formacie innym niż json. Proszę spróbować ponownie.')
            lbl_json.setAlignment(QtCore.Qt.AlignCenter)
            self.layout.addWidget(lbl_json, 1, 0)
        except FileNotFoundError:
            pass
        except:
            pass

    def check_json_structure(self):
        raise NotImplementedError



if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow('Magazyn przerzutowy')
    window.show()
    app.exec()