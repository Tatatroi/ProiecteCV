from REPOSITORY.repository import Meniu
from REPOSITORY.repositoryclient import ListaClienti,Client
import pickle
import functools
from datetime import datetime,timedelta
from colorama import init,Fore
class Comanda:
    def __init__(self, meniu: "Meniu", lista_clienti: ListaClienti):
        self.meniu = meniu
        self.lista_clienti = lista_clienti
        self.lista_comanda_mancare = []
        self.lista_comanda_bauturi = []
        self.lista_preturi = []
        self.lista_timpi = []
        self.nume = ''
        self.adresa = ''

    def alegere_mancare(self):
        self.meniu.afis_mancare()
        input_text = input("Introduceti ID-urile felurilor de mancare dorite separate prin spatii: ")
        lista_indexuri = input_text.split()
        numere = [int(numar) for numar in lista_indexuri]
        with open("meniumancare.pck", "rb") as f:
            lista_mancare = pickle.load(f)
        lista_comanda_mancare = []
        for numar in numere:
            self.lista_comanda_mancare.append(lista_mancare[numar -1].tip_mancare)
            self.lista_preturi.append(lista_mancare[numar -1].pret)
            self.lista_timpi.append(lista_mancare[numar-1].timp_preparare)
        #print(f"Mancaruri: {self.lista_comanda_mancare}")
        return self.lista_comanda_mancare


    def alegere_bauturi(self):
        self.meniu.afis_bautura()
        input_text = input("Introduceti ID-urile felurilor de mancare dorite separate prin spatii: ")
        lista_indexuri = input_text.split()
        numere = [int(numar) for numar in lista_indexuri]
        with open("meniubauturi.pck", "rb") as f:
            lista_mancare = pickle.load(f)
        lista_comanda_bauturi = []
        lista_preturi_bauturi = []
        for numar in numere:
            self.lista_comanda_bauturi.append(lista_mancare[numar -1].tip_bautura)
            self.lista_preturi.append(lista_mancare[numar-1].pret)
        # print(f"Bauturi: + {self.lista_comanda_bauturi}")
        return self.lista_comanda_bauturi

    def verificare_existenta_client(self):
        secventa = input("Introduceti secventa de litere dupa care vrei sa cautati clientul,\n"
                         "aceasta poate sa fie si nume si din adresa: ")
        lista_posibilitati = self.lista_clienti.cautare_client(secventa)
        if not lista_posibilitati:
            print("Nu exista niciun client dupa acest criteriu")
            decizie_ad_client = int(input("Daca doriti sa il adaugati tastati 1, altfel 0"))
            if decizie_ad_client == 1:
                nume_nou = input("Introduceti numele si prenumele clientului: ")
                adresa_noua = input("Introduceti adresa completa: ")
                self.lista_clienti.adaugare_client(Client(nume_nou, adresa_noua))
                self.lista_clienti.salvare_cient()
                self.lista_clienti.incarca_date()
                print("Client adaugat cu succes!")
                print(self.lista_clienti)
            else: return 0
        else:
            # print('Rezultatele cautarii: ')
            # for index, client in enumerate(lista_posibilitati, start=1):
            #     print(f"{index}. {client}")
            return lista_posibilitati


    def calculare_comanda(self):
        total_suma = functools.reduce(lambda a,b:a+b,self.lista_preturi)
        total_timp = functools.reduce(lambda a,b:a+b,self.lista_timpi)
        timp_curent = datetime.now()
        timp_livrare = timp_curent + timedelta(minutes=total_timp)
        print(f"Suma totala a comenzii este: {Fore.LIGHTGREEN_EX}{total_suma} lei{Fore.RESET}\n")
        print(f"Comanda efectuata la ora {timp_curent}, timpul de preparare: {total_timp} minute, estimat livrare {Fore.LIGHTGREEN_EX}{timp_livrare + timedelta(minutes = 20)}{Fore.RESET}\n")
        print("Multumim pentru comanda!")


    def afisare_comanda(self):

        print(self.alegere_mancare())
        print(self.alegere_bauturi())


