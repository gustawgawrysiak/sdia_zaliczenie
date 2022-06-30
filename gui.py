import os

from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QFileDialog,
    QPushButton,
    QLabel,
    QVBoxLayout
)
from warehouse_control_panel.main import run

class FirstWindow(QMainWindow):

    def __init__(self, window_name):
        super().__init__()

        """ustawienie minimalnych wymiarów okna dialogowego
        oraz tytułu okna"""

        self.setMinimumHeight(400)
        self.setMinimumWidth(600)

        self.window_title(window_name)
        container = QWidget()
        self.setCentralWidget(container)

        """utworzenie layoutu oraz umieszczenie w nim
        wszystkich przycisków, linii edycji oraz etykiet"""

        self.layout = QVBoxLayout()

        self.lbl_parcels = QLabel('Aby rozpocząć pracę z programem wybierz 2 pliki .json z paczkami i ciężarówkami')
        self.lbl_parcels.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.lbl_parcels)

        self.btn_load_parcels = QPushButton('Wczytaj plik z paczkami')
        self.layout.addWidget(self.btn_load_parcels)
        self.btn_load_parcels.clicked.connect(self.load_parcels_json)

        self.btn_load_trucks = QPushButton('Wczytaj plik z ciężarówkami')
        self.layout.addWidget(self.btn_load_trucks)
        self.btn_load_trucks.clicked.connect(self.load_trucks_json)

        self.file_trucks = ''
        self.file_parcels = ''

        container.setLayout(self.layout)

    def window_title(self, tytul):
        self.setWindowTitle(tytul)

    def load_parcels_json(self):
        file = QFileDialog.getOpenFileName(self, 'Wskaż plik json', '', 'Plik json (*.json)', 'Plik json (*.json)')
        try:
            path = os.path.normpath(file[0])
            self.file_parcels = path.split(os.sep)[-1]
            if self.file_parcels and self.file_trucks:
                self.start_btn()
        except FileNotFoundError:
            pass

    def load_trucks_json(self):
        file = QFileDialog.getOpenFileName(self, 'Wskaż plik json', '', 'Plik json (*.json)', 'Plik json (*.json)')
        try:
            path = os.path.normpath(file[0])
            self.file_trucks = path.split(os.sep)[-1]
            if self.file_trucks and self.file_parcels:
                self.start_btn()

        except FileNotFoundError:
            pass

    def start_btn(self):
        self.btn_start = QPushButton('Wciśnij, aby rozpocząć skrypt')
        self.layout.addWidget(self.btn_start)
        self.btn_start.clicked.connect(self.hide())

    def hide(self):
        self.lbl_parcels.hide()
        self.btn_load_trucks.hide()
        self.btn_load_parcels.hide()
        self.btn_start.hide()
        # self.window_title('Statystyki')
        self.start()

    def start(self):
        main = run()
        lbl_main = QLabel(f'Całkowity czas wykonywania skryptu: {main.get("main_time"):.5f}')
        self.layout.addWidget(lbl_main)
        lbl_warehouse = QLabel(f'Czas wykonywania skryptu magazynowego: {main.get("warehouse_time"):.5f}')
        self.layout.addWidget(lbl_warehouse)
        lbl_trucks_import = QLabel(f'Czas pobierania pliku .json z ciężarówkami: {main.get("trucks_import_time"):.5f}')
        self.layout.addWidget(lbl_trucks_import)
        lbl_parcels_import = QLabel(f'Czas pobierania pliku .json z paczkami: {main.get("parcels_import_time"):.5f}')
        self.layout.addWidget(lbl_parcels_import)
        lbl_parcels_send = QLabel(f'Liczba wysłanych paczek: {main.get("parcels_send"):d}')
        self.layout.addWidget(lbl_parcels_send)
        lbl_trucks_send = QLabel(f'Liczba wysłanych ciężarówek: {main.get("parcels_send"):d}')
        self.layout.addWidget(lbl_trucks_send)


if __name__ == '__main__':
    app = QApplication([])
    window = FirstWindow('Magazyn przerzutowy')
    window.show()
    app.exec()