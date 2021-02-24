import pickle
import os.path

from listadipendenti.model.ListaDipendenti import ListaDipendenti


class ControlloreListaDipendenti():
    def __init__(self):
        super(ControlloreListaDipendenti, self).__init__()
        self.model = ListaDipendenti()
        if os.path.isfile('listadipendenti/data/lista_dipendenti_salvata.pickle'):
            print("esiste")
            with open('listadipendenti/data/lista_dipendenti_salvata.pickle', 'rb') as f:
                lista_dipendenti_salvata = pickle.load(f)
            self.model = lista_dipendenti_salvata

    def aggiungi_dipendente(self, dipendente):
        self.model.aggiungi_dipendente(dipendente)
        with open('listadipendenti/data/lista_dipendenti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def get_lista_dei_dipendenti(self):
        return self.model.get_lista_dipendenti()

    def get_dipendente_by_index(self, index):
        return self.model.get_dipendente_by_index(index)

    def elimina_dipendente_by_id(self, id):
        self.model.rimuovi_dipendente_by_id(id)
        with open('listadipendenti/data/lista_dipendenti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def save_data(self):
        with open('listadipendenti/data/lista_dipendenti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)