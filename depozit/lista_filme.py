
from domeniu.film import Film


class Filme:
    def __init__(self):
        self._lista = []
        self._adauga_filme()

    def _adauga_filme(self):
        self._lista.append(Film(1, "Gardienii Galaxiei", "film Marvel","acțiune", 2014))
        self._lista.append(Film(2, "Minions","animație pentru copii","animație", 2015))
        self._lista.append(Film(3, "Harry Potter și piatra filozofală","film dupa prima carte din serie,", "film fantastic", 2001))
        self._lista.append(Film(4, "Regele leu","Un leu este conducătorul tuturor animalelor ca rege", "animație", 2019))
        self._lista.append(Film(5, "Frozen","Are la bază un basm scris de Hans Christian Andersen", "animație",2013))

    def adauga(self, film):
        """
        Adauga filme
        :param film: clasa Film
        """
        for f in self._lista:
            if f.id == film.id:
                raise ValueError("Film cu acelasi id e deja in lista")
        self._lista.append(film)

    def cautare_film(self, id_dat):
        """
        Cauta filmul care are un id dat de utilizator
        :param id_dat:tipul int
        :return: filmul
        """
        for film in self._lista:
            if film.id == id_dat:
                return film
        return None

    def sterge(self,film):
        """
        Sterge un film din lista de filme
        :param film: clasa Film
        """
        self._lista.pop(self._lista.index(film))

    def modifica(self,film, id_nou, nume, descriere, gen, an):
        """
        Modifica lista de filme
        :param film: clasa Film
        :param id_nou: tipul int
        :param nume: tipul string
        :param descriere: tipul string
        :param gen: tipul string
        :param an: tipul int

        """
        film.id = id_nou
        film.nume = nume
        film.descriere = descriere
        film.gen = gen
        film.an = an

    def afisare(self):
        """
        Afiseaza lista de filme
        in_str = tipul string
        :return:lista de filme
        """
        in_str = ''
        for film in self._lista:
            in_str += film.afisare() + '\n'
        return in_str

    def get_lista(self):
        return self._lista.copy()

    def __len__(self):
        return len(self._lista)