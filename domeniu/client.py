
class Client:
    def __init__(self, id, nume, cnp, telefon):
        self._id = id
        self._nume = nume
        self._cnp = cnp
        self._telefon = telefon

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valoare):
        self._id = valoare

    @property
    def nume(self):
        return self._nume

    @nume.setter
    def nume(self, nume_nou):
        self._nume = nume_nou

    @property
    def cnp(self):
        return self._cnp

    @cnp.setter
    def cnp(self, cnp_nou):
        self._cnp = cnp_nou

    @property
    def telefon(self):
        return self._telefon

    @telefon.setter
    def telefon(self, telefon_nou):
        self._telefon = telefon_nou

    def afisare(self):
        """
        Afiseazza un client
        """
        return str(self.id) + ' ' + self.nume + ' ' + str(self.cnp) + ' ' + str(self.telefon)