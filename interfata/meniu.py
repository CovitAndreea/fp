from domeniu import film
from functii.functiile_programului import Functii

class Meniu:
    def __init__(self):
        self._functii = Functii()

    def meniu(self):
        print("Meniu")
        print("\n")
        print("Alegeti o comanda: ")
        print("\n")
        print("1.Adauga")
        print("2.Sterge")
        print("3.Modifica")
        print("4.Cauta")
        print("5.Inchiriere/returnare")
        print("6.Rapoarte")
        print("7.Afiseaza")
        print("8.Genereaza random")
        print("x.Iesire")


    def meniu_1(self):
        print("1.Adauga film")
        print("2.Adauga client")


    def meniu_2(self):
        print("1.Sterge film")
        print("2.Sterge client")


    def meniu_3(self):
        print("1.Modifica film")
        print("2.Modifica client")


    def meniu_4(self):
        print("1.Cauta film")
        print("2.Cauta client")


    def meniu_6(self):
        print("1.Clienti cu filme inchiriate ordonate dupa")
        print("2.Cele mai inchiriate filme")
        print("3.Primii 30% clienti cu cele mai multe filme")
        print("4.Cele mai inchiriate genuri")

    def meniu_7(self):
        print("1. Afisare filme")
        print("2. Afisare clienti")
        print("3. Afisare inchirieri")

    def meniu_8(self):
        print("1.Generare filme")
        print("2.Generare clienti")

    def meniu_6_1(self):
        print("1.Nume")
        print("2.Numarul de filme inchiriate")


    def adauga(self):
        self.meniu_1()
        comanda = input('Introduceti optiunea: ')
        if comanda == '1':
            id = int(input('Introduceti id-ul filmului: '))
            nume = input('Introduceti numele filmului: ')
            descriere = input('Introduceti descrierea filmului: ')
            gen = input("Introduceti genul filmului: ")
            an = int(input("Introduceti anul aparitiei: "))
            self._functii.adauga_film(id, nume, descriere, gen, an)
        elif comanda == '2':
            id = int(input('Introduceti id-ul clientului: '))
            nume = input('Introduceti numele clientului: ')
            cnp = int(input('Introduceti cnp-ul clientului: '))
            telefon = int(input('Introduceti numarul de telefon: '))
            self._functii.adauga_client(id, nume, cnp, telefon)

    def sterge(self):
        self.meniu_2()
        comanda = input('Introduceti optiunea: ')
        if comanda == '1':
            id = int(input('Introduceti id-ul filmului: '))
            self._functii.sterge_film(id)
        elif comanda == '2':
            id = int(input('Introduceti id-ul clientului: '))
            self._functii.sterge_client(id)

    def modifica(self):
        self.meniu_3()
        comanda = input('Introduceti optiunea: ')
        if comanda == '1':
            id = int(input('Introduceti id-ul filmului: '))
            id_nou = int(input('Introduceti noul id al filmului: '))
            nume = input('Introduceti numele filmului: ')
            descriere = input('Introduceti descrierea filmului: ')
            gen = input("Introduceti genul filmului: ")
            an = int(input("Introduceti anul aparitiei filmului: "))
            self._functii.modifica_film(id, id_nou, nume, descriere, gen, an)
        elif comanda == '2':
            id = int(input('Introduceti id-ul clientului: '))
            id_nou = int(input('Introduceti noul id clientului: '))
            nume = input('Introduceti numele clientului: ')
            cnp = int(input('Introduceti cnp-ul clientului: '))
            telefon = int(input('Introduceti numarul de telefon: '))
            self._functii.modifica_client(id, id_nou, nume, cnp, telefon)

    def cauta(self):
        self.meniu_4()
        comanda = input('Introduceti optiunea: ')
        if comanda == '1':
            id = int(input('Introduceti id-ul filmului: '))
            film = self._functii.cautare_film(id)
            print(film.afisare())
        elif comanda == '2':
            id = int(input('Introduceti id-ul clientului: '))
            client = self._functii.cautare_client(id)
            print(client.afisare())

    def inchiriere_returnare(self):
        id_client = int(input('Introduceti id-ul clientului: '))
        id_film = int(input('Introduceti id-ul filmului: '))
        zi_inchiriere = int(input('Introduceti ziua inchirierii filmului: '))
        luna_inchiriere = int(input('Introduceti luna inchirierii filmului: '))
        an_inchiriere = int(input('Introduceti anul inchirierii filmului: '))
        zi_returnare = int(input('Introduceti ziua returnarii filmului: '))
        luna_returnare = int(input('Introduceti luna returnarii filmului: '))
        an_returnare = int(input('Introduceti anul returnarii filmului: '))
        self._functii.inchiriat_returnat(id_client, id_film, zi_inchiriere, luna_inchiriere, an_inchiriere, zi_returnare, luna_returnare, an_returnare)

    def rapoarte(self):
        self.meniu_6()
        comanda = input("Introduceti optiunea: ")
        if comanda == '1':
            self.meniu_6_1()
            comanda = input("Introduceti optiunea: ")
            if comanda == '1':
                 for client in self._functii.clienti_ordonati_dupa_nume():
                     print(client)
            if comanda == '2':
                for client in self._functii.clienti_ordonati_dupa_numar_filme():
                    print(client)
        elif comanda == '2':
            for film in self._functii.cele_mai_inchiriate_filme():
                print(film)
        elif comanda == '3':
            for client in self._functii.primii_30_la_suta_cele_mai_multe_filme():
                print(client)
        elif comanda == '4':
            for gen in self._functii.cele_mai_inchiriate_genuri():
                print(gen)

    def generare_random(self):
        self.meniu_8()
        comanda = input("Introduceti optiunea: ")
        if comanda == '1':
            generare_filme = int(input("Introduceti numarul filmelor pe care vreti sa il generati: "))
            self._functii.random_f(generare_filme)
        if comanda == '2':
            generare_clienti = int(input("Introduceti numarul clientilor pe care vreti sa il generati: "))
            self._functii.random_c(generare_clienti)

    def afisare(self):
        self.meniu_7()
        comanda = input('Introduceti optiunea: ')
        if comanda == '1':
            print(self._functii.afisare_filme())
        elif comanda == '2':
            print(self._functii.afisare_clienti())
        elif comanda == '3':
            print(self._functii.afisare_inchirieri())


    def start(self):

        ruleaza = True
        dic_comenzi = {'1': self.adauga, '2': self.sterge, '3': self.modifica, '4': self.cauta, '5': self.inchiriere_returnare, '6': self.rapoarte, '7': self.afisare, '8':self.generare_random}
        while ruleaza:
            self.meniu()
            comanda = input('Introduceti comanda: ')
            if comanda in dic_comenzi:
                try:
                    dic_comenzi[comanda]()
                except ValueError as ve:
                    print(str(ve))
            elif comanda == 'x':
                ruleaza = False
            else:
                print("Comanda gresita")

if __name__ == '__main__':
    meniu = Meniu()
    meniu.start()