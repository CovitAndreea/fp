
from domeniu.client import Client


class Clienti:
    def __init__(self):
        self._lista = []
        self._adauga_clienti()

    def _adauga_clienti(self):
        self._lista.append(Client(1, "Popescu Elena", 6020203152134, 4071215141215))
        self._lista.append(Client(2, "Ionescu Marian", 5030402156123, 40745151485))
        self._lista.append(Client(3, "Cojocaru Ștefan", 5020305123145, 40745859423))
        self._lista.append(Client(4, "Trandafir Iulia", 6100205152124, 40785946832))
        self._lista.append(Client(5, "Popescu Maria", 6010504125145, 40715121415))

    def adauga(self, client):
        """
        Adauga clienti
        :param client: clasa Client
        """
        for c in self._lista:
            if c.id == client.id:
                raise ValueError("Client cu acelasi id e deja in lista")
        self._lista.append(client)

    def cautare_client(self, id_dat):
        """
        Cauta clientul care are un id dat de utilizator
        :param id_dat:tipul int
        :return: clientul
        """
        for client in self._lista:
            if client.id == id_dat:
                return client
        return None

    def sterge (self, client):
        """
       Sterge un client din lista de clienti
        :param client: clasa Client
        """
        self._lista.pop(self._lista.index(client))

    def modifica(self, client, id_nou, nume, cnp, telefon):
        """

        :param client:clasa client
        :param id_nou: tipul int
        :param nume: tipul string
        :param cnp: tipul int
        :param telefon: tipul int

        """
        client.id = id_nou
        client.nume = nume
        client.cnp = cnp
        client.telefon = telefon

    def afisare(self):
        """
       Afiseaza lista de clienti
        in_str = tipul string
        :return:lista de clienti
        """
        in_str = ''
        for client in self._lista:
            in_str += client.afisare() + '\n'
        return in_str

    def get_lista(self):
        return self._lista.copy()

    def __len__(self):
        return len(self._lista)
