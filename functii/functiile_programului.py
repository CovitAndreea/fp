from depozit.lista_clienti import Clienti
from depozit.lista_filme import Filme
from depozit.lista_inchirieri import Inchirieri
from domeniu.film import Film
from domeniu.client import Client
from domeniu.inchiriere import Inchiriere
from Validare.validatori import ValidatorClient, ValidatorFilm,ValidatorInchiriere
import datetime
import random
import string


class Functii:
    def __init__(self):
        self._filme = Filme()
        self._clienti = Clienti()
        self._inchirieri = Inchirieri()
        test_init(self._clienti, self._filme, self._inchirieri)
        self._validare_client = ValidatorClient()
        self._validare_film = ValidatorFilm()
        self._validare_inchiriere = ValidatorInchiriere()

    def adauga_film(self, id, nume, descriere, gen, an):
        self._validare_film.valideaza(Film(id, nume, descriere, gen,an))
        self._filme.adauga(Film(id, nume, descriere, gen,an))

    def adauga_client(self, id, nume, cnp, telefon):
        self._validare_client.valideaza_client(Client(id, nume, cnp,telefon))
        self._clienti.adauga(Client(id, nume, cnp,telefon))

    def sterge_film(self, id):
        film = self._filme.cautare_film(id)
        if film == None:
            raise ValueError('Film inexistent')
        self._filme.sterge(film)

    def sterge_client(self, id):
        client = self._clienti.cautare_client(id)
        if client == None:
            raise ValueError('Client inexistent')
        self._clienti.sterge(client)

    def modifica_film(self, id, id_nou, nume, descriere, gen, an):
        self._validare_film.valideaza(Film(id_nou, nume, descriere, gen, an))
        film = self._filme.cautare_film(id)
        if film == None:
            raise ValueError('Film inexistent')
        self._filme.modifica(film, id_nou, nume, descriere, gen, an)

    def modifica_client(self, id, id_nou, nume, cnp, telefon):
        self._validare_client.valideaza_client(Client(id_nou, nume, cnp, telefon))
        client = self._clienti.cautare_client(id)
        if client == None:
            raise ValueError('Client inexistent')
        self._clienti.modifica(client, id_nou, nume, cnp, telefon)

    def cautare_film(self, id):
        film = self._filme.cautare_film(id)
        if film == None:
            raise ValueError('Film inexistent')
        return film

    def cautare_client(self, id):
        client = self._clienti.cautare_client(id)
        if client == None:
            raise ValueError('Client inexistent')
        return client

    def inchiriat_returnat(self, id_client, id_film, zi_inchiriere, luna_inchiriere, an_inchiriere, zi_returnare, luna_returnare, an_returnare):
        client = self._clienti.cautare_client(id_client)
        if client == None:
            raise ValueError('Client inexistent')
        film = self._filme.cautare_film(id_film)
        if film == None:
            raise ValueError('Film inexistent')
        data_inchiriere = datetime.date(an_inchiriere, luna_inchiriere, zi_inchiriere)
        data_returnare = datetime.date(an_returnare, luna_returnare, zi_returnare)
        self._validare_inchiriere.valideaza_inchiriere(Inchiriere(client, film, data_inchiriere, data_returnare))
        self._inchirieri.adauga_inchirierea(Inchiriere(client, film, data_inchiriere, data_returnare))

    def clienti_ordonati_dupa_nume(self):
        """
        Afiseaza clientii ordonati dupa nume(alfabetic)
        lista = clasa list
        :return:lista
        """
        dict_clienti = {}
        lista = []
        for inchiriere in self._inchirieri.get_lista():
            if inchiriere.client not in dict_clienti:
                dict_clienti[inchiriere.client] = 1
            else:
                dict_clienti[inchiriere.client] +=1
        for client in dict_clienti:
            lista.append(ClientInchirieri(client, dict_clienti[client]))

        lista.sort(key = (lambda a: a.client.nume))
        return lista

    def clienti_ordonati_dupa_numar_filme(self):
        """
        Afiseaza clientii ordonati dupa numar de filme inchiriate
        lista = clasa list
        :return: lista
        """
        dict_clienti = {}
        lista = []
        for inchiriere in self._inchirieri.get_lista():
            if inchiriere.client not in dict_clienti:
                dict_clienti[inchiriere.client] = 1
            else:
                dict_clienti[inchiriere.client] += 1
        for client in dict_clienti:
            lista.append(ClientInchirieri(client, dict_clienti[client]))

        lista.sort(key=(lambda a: a.nr_inchirieri), reverse=True)
        return lista


    def cele_mai_inchiriate_filme(self):
        """
        Afiseaza filmele in ordine descrescatoare a numarului de inchirieri
        lista = clasa list
        :return: lista
        """
        dict_filme = {}
        lista = []
        for inchiriere in self._inchirieri.get_lista():
            if inchiriere.film not in dict_filme:
                dict_filme[inchiriere.film] = 1
            else:
                dict_filme[inchiriere.film] += 1
        for client in dict_filme:
            lista.append(ClientInchirieri(client, dict_filme[client]))

        lista.sort(key=(lambda a: a.nr_inchirieri), reverse=True)
        return lista

    def primii_30_la_suta_cele_mai_multe_filme(self):
        """
        Afiseaza primii 30% cu cele mai multe filme
        lista = clasa list
        :return:lista
        """
        dict_clienti = {}
        lista = []
        for inchiriere in self._inchirieri.get_lista():
            if inchiriere.client not in dict_clienti:
                dict_clienti[inchiriere.client] = 1
            else:
                dict_clienti[inchiriere.client] += 1
        for client in dict_clienti:
            lista.append(ClientInchirieri(client, dict_clienti[client]))

        lista.sort(key=(lambda a: a.nr_inchirieri), reverse=True)
        return lista[:(int(3/10*len(self._clienti)) if 3/10*len(self._clienti) >= 1 else 1)]



    def cele_mai_inchiriate_genuri(self):
       
        dict_filme = {}
        lista = []
        for inchiriere in self._inchirieri.get_lista():
            if inchiriere.film.gen not in dict_filme:
                dict_filme[inchiriere.film.gen] = 1
            else:
                dict_filme[inchiriere.film.gen] += 1
        for gen in dict_filme:
            lista.append(GenInchirieri(gen, dict_filme[gen]))

        lista.sort(key=(lambda a: a.nr_inchirieri), reverse=True)
        return lista

    def random_f(self, generare_filme):
        """

        :param generare_filme:i, id, generare_filme = numere naturale, litere, nume, descriere, gen = sir de caractere

        """
        i = 1
        litere = string.ascii_lowercase
        while i <= generare_filme:
            id = random.randint(1, 200)
            nume = ''.join(random.choices(litere, k=random.randint(5, 10)))
            descriere = ''.join(random.choices(litere, k=random.randint(20, 30)))
            gen = ''.join(random.choices(litere, k=random.randint(3, 5)))
            an = random.randint(1950, 2020)
            try:
                self.adauga_film(id, nume, descriere, gen, an)
            except ValueError:
                i -= 1
            i += 1

    def random_c(self, generare_clienti):
        """

        :param generare_clienti: i, id, cnp, telefon, generare_clienti = numere naturale, litere, nume = sir de caractere

        """
        i = 1
        litere = string.ascii_lowercase
        while i <= generare_clienti:
            id = random.randint(1, 200)
            nume = ''.join(random.choices(litere, k=random.randint(7, 15)))
            cnp = random.randint(5000000000000, 9999999999999)
            telefon = random.randint(1000000000, 9999999999)
            try:
                self.adauga_client(id, nume, cnp, telefon)
            except ValueError:
                i -= 1
            i += 1

    def afisare_inchirieri(self):
        return self._inchirieri.afisare()

    def afisare_filme(self):
        return self._filme.afisare()

    def afisare_clienti(self):
        return self._clienti.afisare()

    def lungime_filme(self):
        return len(self._filme)

    def lungime_clienti(self):
        return len(self._clienti)

    def lungime_inchirieri(self):
        return len(self._inchirieri)






class ClientInchirieri:
    def __init__(self, client, nr_inchirieri):
        self._client = client
        self._nr_inchirieri = nr_inchirieri

    @property
    def client(self):
        return self._client

    @property
    def nr_inchirieri(self):
        return self._nr_inchirieri

    def __str__(self):
        return self._client.nume + ' - ' + str(self._nr_inchirieri)

class FilmInchirieri:
    def __init__(self, film, nr_inchirieri):
        self._film = film
        self._nr_inchirieri = nr_inchirieri

    @property
    def film(self):
        return self._film

    @property
    def nr_inchirieri(self):
        return self._nr_inchirieri

    def __str__(self):
        return self._film.nume + ' - ' + str(self._nr_inchirieri)

class GenInchirieri:
    def __init__(self, gen, nr_inchirieri):
        self._gen = gen
        self._nr_inchirieri = nr_inchirieri

    @property
    def gen(self):
        return self._gen

    @property
    def nr_inchirieri(self):
        return self._nr_inchirieri

    def __str__(self):
        return self._gen + ' - ' + str(self._nr_inchirieri)


def test_init(clienti, filme, inchirieri):
    lista_clienti = clienti.get_lista()
    lista_filme = filme.get_lista()
    inchirieri.adauga_inchirierea(Inchiriere(lista_clienti[0], lista_filme[1], datetime.date(2020, 10, 5), datetime.date(2020, 10, 9)))
    inchirieri.adauga_inchirierea(Inchiriere(lista_clienti[1], lista_filme[2], datetime.date(2020, 7, 8), datetime.date(2020, 7, 15)))
    inchirieri.adauga_inchirierea(Inchiriere(lista_clienti[2], lista_filme[3], datetime.date(2019, 12, 20), datetime.date(2019, 12, 23)))
    inchirieri.adauga_inchirierea(Inchiriere(lista_clienti[3], lista_filme[4], datetime.date(2018, 12, 8), datetime.date(2020, 12, 12)))
    inchirieri.adauga_inchirierea(Inchiriere(lista_clienti[4], lista_filme[1], datetime.date(2020, 9, 20), datetime.date(2020,9, 25)))
    inchirieri.adauga_inchirierea(Inchiriere(lista_clienti[1], lista_filme[0], datetime.date(2020, 1, 1), datetime.date(2020, 1, 3)))
    inchirieri.adauga_inchirierea(Inchiriere(lista_clienti[2], lista_filme[0], datetime.date(2020, 2, 2), datetime.date(2020, 2, 5)))
    inchirieri.adauga_inchirierea(Inchiriere(lista_clienti[3], lista_filme[0], datetime.date(2020, 3, 4), datetime.date(2020, 3, 5)))
    inchirieri.adauga_inchirierea(Inchiriere(lista_clienti[1], lista_filme[1], datetime.date(2020, 5, 6), datetime.date(2020, 5, 7)))
    inchirieri.adauga_inchirierea(Inchiriere(lista_clienti[2], lista_filme[1], datetime.date(2020, 8, 9), datetime.date(2020, 8, 11)))
    inchirieri.adauga_inchirierea(Inchiriere(lista_clienti[0], lista_filme[2], datetime.date(2020, 5, 9), datetime.date(2020, 5, 10)))

def test_adauga_film():
    functii = Functii()
    lungime = functii.lungime_filme()
    functii.adauga_film(7 ,"Star Wars", "Razbouiul stelelor", "actiune", 1975)
    assert functii.lungime_filme() == lungime+1
    film_nou = functii.cautare_film(7)
    assert film_nou.nume == "Star Wars" and film_nou.descriere == "Razbouiul stelelor" and film_nou.gen == "actiune" and film_nou.an == 1975
    try:
        functii.adauga_film(7 ,"Star Wars", "Razbouiul stelelor", "actiune", 1975)
        assert False
    except ValueError:
        assert True


def test_adauga_client():
    functii = Functii()
    lungime = functii.lungime_clienti()
    functii.adauga_client(7, "Popescu Maria", 6010503125145, 40256318965)
    assert functii.lungime_clienti() == lungime+1
    client_nou = functii.cautare_client(7)
    assert client_nou.nume == "Popescu Maria" and client_nou.cnp == 6010503125145 and client_nou.telefon == 40256318965
    try:
        functii.adauga_client(7, "Popescu Maria", 6010503125145, 40256318965)
        assert False
    except ValueError:
        assert True

def test_sterge_film():
    functii = Functii()
    lungime = functii.lungime_filme()
    functii.sterge_film(1)
    assert functii.lungime_filme() == lungime-1
    try:
        functii.sterge_film(7)
        assert False
    except ValueError:
        assert True

def test_sterge_client():
    functii = Functii()
    lungime = functii.lungime_clienti()
    functii.sterge_client(1)
    assert functii.lungime_clienti() == lungime-1
    try:
        functii.sterge_client(7)
        assert False
    except ValueError:
        assert True

def test_modifica_film():
    functii = Functii()
    functii.modifica_film(2, 8, "Star Wars 2", "Continuarea razboiul stelelor", "actiune", 1978)
    film_modificat = functii.cautare_film(8)
    assert film_modificat.nume == "Star Wars 2" and film_modificat.descriere== "Continuarea razboiul stelelor" and film_modificat.gen == "actiune" and film_modificat.an == 1978
    try:
        functii.modifica_film(2, 8, "Star Wars 2", "Continuarea razboiul stelelor", "actiune", 1978)
        assert False
    except ValueError:
        assert True

def test_modifica_client():
    functii = Functii()
    functii.modifica_client(2, 9, "Popescu Lavinia", 601020345679, 4075611545645)
    client_modificat = functii.cautare_client(9)
    assert client_modificat.nume == "Popescu Lavinia" and client_modificat.cnp == 601020345679 and client_modificat.telefon == 4075611545645
    try:
        functii.modifica_client(2, 9, "Popescu Lavinia", 601020345679, 4075611545645)
        assert False
    except ValueError:
        assert True

def test_cautare_film():
    functii = Functii()
    film = functii.cautare_film(3)
    assert film.nume == "Harry Potter și piatra filozofală" and film.descriere== "film dupa prima carte din serie" and film.gen == "film fantastic" and film.an == 2001
    try:
        functii.cautare_film(10)
        assert False
    except ValueError:
        assert True

def test_cautare_client():
    functii = Functii()
    client = functii.cautare_client(3)
    assert client.nume == "Cojocaru Ștefan" and client.cnp == 5020305123145 and client.telefon == 40745859423
    try:
        functii.cautare_client(11)
        assert False
    except ValueError:
        assert True

def test_inchiriat_returnat():
    functii = Functii()
    lungime = functii.lungime.inchirieri
    functii.inchiriat_returnat(2, 2, 15, 2, 2020, 20, 2, 2020)
    assert functii.lungime_clienti() == lungime + 1

def test_clienti_ordonati_dupa_nume():
    functii = Functii()
    lista = functii.clienti_ordonati_dupa_nume()
    assert lista[0].client.nume == "Cojocaru Ștefan" and lista[0].client.cnp == 5020305123145 and lista[0].client.telefon == 40745859423

def test_clienti_ordonati_dupa_numar_filme():
    functii = Functii()
    lista = functii.clienti_ordonati_dupa_numar_filme()
    assert lista[0].client.nume == "Ionescu Marian" and lista[0].client.cnp == 5030402156123 and lista[0].client.telefon == 40745151485

def test_cele_mai_inchiriate_filme():
    functii = Functii()
    lista = functii.cele_mai_inchiriate_filme()
    assert lista[0].film.nume == "Minions" and lista[0].film.descriere =="animație pentru copii"  and lista[0].film.gen == "animație" and lista[0].film.an == 2015

def test_primii_30_la_suta_cele_mai_multe_filme():
    functii = Functii()
    lista = functii.clienti_ordonati_dupa_nume()
    assert lista[0].client.nume == "Ionescu Marian" and lista[0].client.cnp == 5030402156123 and lista[0].client.telefon == 40745151485

if __name__ == '__main__':    
    test_adauga_client()
    test_adauga_film()
    test_sterge_film()
    test_sterge_client()
    test_modifica_film()
    test_modifica_client()
    test_cautare_film()
    test_cautare_client()
    test_inchiriat_returnat()
    test_clienti_ordonati_dupa_nume()
    test_clienti_ordonati_dupa_numar_filme()
    test_cele_mai_inchiriate_filme()
    test_primii_30_la_suta_cele_mai_multe_filme()