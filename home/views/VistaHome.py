from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from listaclienti.view.VistaListaClienti import VistaListaClienti
from listadipendenti.view.VistaListaDipendenti import VistaListaDipendenti
from listaprenotazioni.view.VistaListaPrenotazioni import VistaListaPrenotazioni
from listaservizi.view.VistaListaServizi import VistaListaServizi


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        grid_layout = QGridLayout()

        servizi_button = QPushButton("Lista Servizi")
        servizi_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        servizi_button.clicked.connect(self.go_lista_servizi)
        clienti_button = QPushButton('Lista Clienti')
        clienti_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        clienti_button.clicked.connect(self.go_lista_clienti)
        dipendenti_button = QPushButton('Lista Dipendenti')
        dipendenti_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        dipendenti_button.clicked.connect(self.go_lista_dipendenti)
        prenotazioni_button = QPushButton('Lista Prenotazioni')
        prenotazioni_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        prenotazioni_button.clicked.connect(self.go_lista_prenotazioni)

        grid_layout.addWidget(servizi_button, 0, 0)
        grid_layout.addWidget(clienti_button, 0, 1)
        grid_layout.addWidget(dipendenti_button, 1, 0)
        grid_layout.addWidget(prenotazioni_button, 1, 1)
        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle('Gestore Stabilimento PRO')

    def go_lista_servizi(self):
        self.vista_lista_servizi = VistaListaServizi()
        self.vista_lista_servizi.show()

    def go_lista_prenotazioni(self):
        self.vista_lista_prenotazioni = VistaListaPrenotazioni()
        self.vista_lista_prenotazioni.show()

    def go_lista_dipendenti(self):
        self.vista_lista_dipendenti = VistaListaDipendenti()
        self.vista_lista_dipendenti.show()

    def go_lista_clienti(self):
        self.vista_lista_clienti = VistaListaClienti()
        self.vista_lista_clienti.show()