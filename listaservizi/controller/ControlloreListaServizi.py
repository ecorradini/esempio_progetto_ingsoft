import pickle
import os.path
import json

from listaservizi.model.ListaServizi import ListaServizi
from servizio.model.Servizio import Servizio


class ControlloreListaServizi():
    def __init__(self):
        super(ControlloreListaServizi, self).__init__()
        self.model = ListaServizi()
        if os.path.isfile('listaservizi/data/lista_servizi_salvata.pickle'):
            print("esiste")
            with open('listaservizi/data/lista_servizi_salvata.pickle', 'rb') as f:
                lista_servizi_salvata = pickle.load(f)
            self.model = lista_servizi_salvata
        else:
            print("non esiste")
            with open('listaservizi/data/lista_servizi_iniziali.json') as f:
                lista_servizi_iniziale = json.load(f)
            for servizio in lista_servizi_iniziale:
                self.model.aggiungi_servizio(Servizio(servizio["id"], servizio["nome"], servizio["tipo"], servizio["posizione"], servizio["prezzo"]))
            with open('listaservizi/data/lista_servizi_salvata.pickle', 'wb') as handle:
                pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def get_lista_dei_servizi(self):
        return self.model.get_lista_servizi()

    def get_servizio_by_index(self, index):
        return self.model.get_servizio_by_index(index)