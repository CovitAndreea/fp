
class Inchiriere:
    def __init__(self, client, film, data_inchiriere, data_returnare):
        self._client = client
        self._film = film
        self._data_inchiriere = data_inchiriere
        self._data_returnare = data_returnare

    @property
    def client(self):
        return self._client

    @property
    def film(self):
        return self._film

    @property
    def data_inchiriere(self):
        return self._data_inchiriere

    @property
    def data_returnare(self):
        return self._data_returnare

    def afisare(self):
        """
        Afiseaza o inchiriere
        """
        return self._client.nume + ' ' + self._film.nume + ' ' + str(self._data_inchiriere) + ' ' + str(self._data_returnare)