class ListaServizi():
    def __init__(self):
        super(ListaServizi, self).__init__()
        self.lista_servizi = []

    def aggiungi_servizio(self, servizio):
        self.lista_servizi.append(servizio)

    def get_servizio_by_index(self, index):
        return self.lista_servizi[index]

    def get_lista_servizi(self):
        return self.lista_servizi