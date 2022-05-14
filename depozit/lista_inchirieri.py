

class Inchirieri:
    def __init__(self):
        self._lista = []

    def adauga_inchirierea(self, inchiriere):
        """
        Adauga o inchiriere
        :param inchiriere: i = numar natural

        """
        for i in self._lista:
            if i.film.id == inchiriere.film.id and i.data_inchiriere < inchiriere.data_inchiriere < i.data_returnare:
                raise ValueError("Filmul este deja inchiriat")
        self._lista.append(inchiriere)

    def afisare(self):
        """
        Afiseaza lista de inchirieri
        in_str = tipul string
        :return:lista de inchirieri
        """
        in_str = ''
        for inchiriere in self._lista:
            in_str += inchiriere.afisare() + '\n'
        return in_str

    def get_lista(self):
        return self._lista.copy()

    def __len__(self):
        return len(self._lista)