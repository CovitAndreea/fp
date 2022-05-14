
class Film:
    def __init__(self, id, nume, descriere, gen, an):
        self._id = id
        self._nume = nume
        self._descriere = descriere
        self._gen = gen
        self._an = an

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
    def nume(self,nume_nou):
        self._nume = nume_nou

    @property
    def descriere(self):
        return self._descriere

    @descriere.setter
    def descriere(self, descriere_noua):
         self._descriere = descriere_noua

    @property
    def gen(self):
        return self._gen

    @gen.setter
    def gen(self, gen_nou):
        self._gen = gen_nou

    @property
    def an(self):
        return self._an

    @an.setter
    def an(self, an_nou):
        self._an = an_nou

    def afisare(self):
        """
        Afiseaza un film

        """
        return str(self.id) + ' ' + self.nume + ' ' + self.descriere + ' ' + self.gen + ' ' + str(self.an)