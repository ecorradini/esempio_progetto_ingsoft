from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QSpacerItem, QSizePolicy, QMessageBox

from dipendente.model.Dipendente import Dipendente


class VistaInserisciDipendente(QWidget):
    def __init__(self, controller, callback):
        super(VistaInserisciDipendente, self).__init__()
        self.controller = controller
        self.callback = callback

        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel("Nome"))
        self.text_nome = QLineEdit(self)
        v_layout.addWidget(self.text_nome)

        v_layout.addWidget(QLabel("Cognome"))
        self.text_cognome = QLineEdit(self)
        v_layout.addWidget(self.text_cognome)

        v_layout.addWidget(QLabel("Codice Fiscale"))
        self.text_cf = QLineEdit(self)
        v_layout.addWidget(self.text_cf)

        v_layout.addWidget(QLabel("Data di nascita (dd/MM/yyyy)"))
        self.text_datanascita = QLineEdit(self)
        v_layout.addWidget(self.text_datanascita)

        v_layout.addWidget(QLabel("Luogo di nascita"))
        self.text_luogonascita = QLineEdit(self)
        v_layout.addWidget(self.text_luogonascita)

        v_layout.addWidget(QLabel("Email"))
        self.text_email = QLineEdit(self)
        v_layout.addWidget(self.text_email)

        v_layout.addWidget(QLabel("Telefono"))
        self.text_telefono = QLineEdit(self)
        v_layout.addWidget(self.text_telefono)

        v_layout.addWidget(QLabel("Licenza"))
        self.text_licenza = QLineEdit(self)
        v_layout.addWidget(self.text_licenza)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.add_dipendente)
        v_layout.addWidget(btn_ok)

        self.setLayout(v_layout)
        self.setWindowTitle('Nuovo Dipendente')

    def add_dipendente(self):
        nome = self.text_nome.text()
        cognome = self.text_cognome.text()
        cf = self.text_cf.text()
        datanascita = self.text_datanascita.text()
        luogonascita = self.text_luogonascita.text()
        email = self.text_email.text()
        telefono = self.text_telefono.text()
        licenza = self.text_licenza.text()
        if(nome == "" or cognome == "" or cf == "" or datanascita == "" or luogonascita == "" or email == "" or telefono == "" or licenza == ""):
            QMessageBox.critical(self, 'Errore', "Per favore, inserisci tutte le informazioni richieste", QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_dipendente(Dipendente((nome+cognome).lower(), nome, cognome, cf, datanascita, luogonascita, email, telefono, licenza))
            self.callback()
            self.close()
