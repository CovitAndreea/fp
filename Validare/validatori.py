from domeniu.film import Film
from domeniu.client import Client
from domeniu.inchiriere import Inchiriere
import  datetime

class ValidatorFilm:
    def __init__(self):
        pass
    def valideaza(self, film):
        """
        Arunca exceptii de tipul ValidationException
        :param film: un film

        """

        error = ""
        id = film.id
        nume = film.nume
        descriere = film.descriere
        gen = film.gen
        an = film.an
        if id <= 0:
            error += "Id invalid\n"
        if nume == "":
            error +="Nume invalid\n"
        if descriere =="":
            error +="Descriere invalida\n"
        if gen == "":
            error += "Gen invalid\n"
        if an <= 0:
            error += "An invalid\n"
        if len(error) > 0:
            raise ValueError(error)

class ValidatorClient:
    def __init__(self):
        pass

    def valideaza_client(self, client):
        """
        Arunca exceptii de tipul ValidationException
        :param client: un client

        """
        error = ""
        id = client.id
        nume = client.nume
        cnp = client.cnp
        telefon = client.telefon
        if id <= 0:
            error += "Id invalid\n"
        if nume == "":
            error += "Nume invalid\n"
        if cnp <= 0:
            error += "Cnp invalid\n"
        if telefon <= 0:
            error += "Numar telefon invalid\n"
        if len(error) > 0:
            raise ValueError(error)

class ValidatorInchiriere:
    def __init__(self):
        pass

    def valideaza_inchiriere(self, inchiriere):
        """
        Arunca exceptii de tipul ValidationException
        :param inchiriere: o inchiriere

        """
        error = ''
        if inchiriere.data_inchiriere > inchiriere.data_returnare:
            error += "Nu este posibil sa returnezi un film inainte sa il inchiriezi"
        if len(error) > 0:
            raise ValueError(error)

def test_validator_film():
    val_film = ValidatorFilm()

    val_film.valideaza(Film(7, 'efwf', 'regerh', 'erhrth', 1998))

    try:
        val_film.valideaza(Film(-4, 'erg', 'erge', 'thth', 3463))
        assert False
    except ValueError:
        assert True

    try:
        val_film.valideaza(Film(4, '', '', '', 3254))
        assert False
    except ValueError:
        assert True

    try:
        val_film.valideaza(Film(5, 'eherh', 'erher', 'eryyu', 0))
        assert False
    except ValueError:
        assert True

def test_validator_client():
    val_client = ValidatorClient()

    val_client.valideaza_client(Client(8, 'Popescu Maria', 6010503125145, 40785748532))

    try:
        val_client.valideaza_client(Client(-5,'Ionescu Emilia', 6040502154125, 40728456875))
        assert  False
    except ValueError:
        assert True

    try:
        val_client.valideaza_client(Client(8,'',6589745555, 40457454648))
        assert False
    except ValueError:
        assert True

def test_validator_inchiriere():
    val_inchiriere = ValidatorInchiriere()

    val_inchiriere.valideaza_inchiriere(Inchiriere(4, 5, datetime.date(2020, 5, 14), datetime.date(2020, 5, 17)))

    try:
        val_inchiriere.valideaza_inchiriere(Inchiriere(-4, 5, datetime.date(2020, 7, 17), datetime.date(2020, 7, 14)))
        assert False
    except ValueError:
        assert True

    try:
        val_inchiriere.valideaza_inchiriere(Inchiriere(4, 5, datetime.date(2020, 7, 17), datetime.date(2020, 7, 32)))
        assert False
    except ValueError:
        assert True

if __name__ == '__main__':
    test_validator_film()
    test_validator_client()
    test_validator_inchiriere()