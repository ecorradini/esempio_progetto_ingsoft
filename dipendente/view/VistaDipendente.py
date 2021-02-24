from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy

from abbonamento.view.VistaAbbonamento import VistaAbbonamento
from cliente.controller.ControlloreCliente import ControlloreCliente
from dipendente.controller.ControlloreDipendente import ControlloreDipendente


class VistaDipendente(QWidget):
    def __init__(self, dipendente, elimina_dipendente, elimina_callback, parent=None):
        super(VistaDipendente, self).__init__()
        self.controller = ControlloreDipendente(dipendente)
        self.elimina_dipendente = elimina_dipendente
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_nome = QLabel(self.controller.get_nome_dipendente() + " " + self.controller.get_cognome_dipendente())
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label_cf = QLabel("Codice Fiscale: {}".format(self.controller.get_cf_dipendente()))
        font_cf = label_cf.font()
        font_cf.setPointSize(17)
        label_cf.setFont(font_cf)
        v_layout.addWidget(label_cf)

        label_datanascita = QLabel("Data Nascita: {}".format(self.controller.get_datanascita_dipendente()))
        font_datanascita = label_datanascita.font()
        font_datanascita.setPointSize(17)
        label_datanascita.setFont(font_datanascita)
        v_layout.addWidget(label_datanascita)

        label_luogonascita = QLabel("Luogo Nascita: {}".format(self.controller.get_luogonascita_dipendente()))
        font_luogonascita = label_luogonascita.font()
        font_luogonascita.setPointSize(17)
        label_luogonascita.setFont(font_luogonascita)
        v_layout.addWidget(label_luogonascita)

        label_email = QLabel("Email: {}".format(self.controller.get_email_dipendente()))
        font_email = label_email.font()
        font_email.setPointSize(17)
        label_email.setFont(font_email)
        v_layout.addWidget(label_email)

        label_telefono = QLabel("Telefono: {}".format(self.controller.get_telefono_dipendente()))
        font_telefono = label_telefono.font()
        font_telefono.setPointSize(17)
        label_telefono.setFont(font_telefono)
        v_layout.addWidget(label_telefono)

        label_licenza = QLabel("Età: {}".format(self.controller.get_licenza_dipendente()))
        font_licenza = label_licenza.font()
        font_licenza.setPointSize(17)
        label_licenza.setFont(font_licenza)
        v_layout.addWidget(label_licenza)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_dipendente_click)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle(dipendente.nome)

    def elimina_dipendente_click(self):
        self.elimina_dipendente(self.controller.get_id_dipendente())
        self.elimina_callback()
        self.close()