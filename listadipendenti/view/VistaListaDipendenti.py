from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy


class VistaListaDipendenti(QWidget):
    def __init__(self, parent=None):
        super(VistaListaDipendenti, self).__init__(parent)
        grid_layout = QGridLayout()
        self.setLayout(grid_layout)
        self.resize(600, 600)
        self.setWindowTitle('Lista Dipendenti')