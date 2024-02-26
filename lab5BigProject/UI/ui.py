from REPOSITORY.repository import Meniu,Mancare,Bautura
from REPOSITORY.repositoryclient import ListaClienti,Client
from CONTROLLER.controller import Comanda
from colorama import init,Fore
class Ui:
    def __init__(self,meniu:"Meniu",listaclienti:"ListaClienti",comanda:"Comanda"):
        self.meniu = meniu
        self.listaclienti = listaclienti
        self.comanda = comanda

    def optiunea1(self):
        self.meniu.afis_mancare()
        while True:
            print('''
            
            Daca doriti sa faceti modificari aveti urmatoarele variante:
            
            1 - Adaugare element in meniul de mancare
            2 - Modificare element in meniul de mancare
            3 - Stergere element in meniul de mancare
            4 - Nu se efectueaza nicio operatie
            
            ''')

            optiune = int(input("Tastati optiunea: "))

            if optiune == 1:
                tip_mancare_noua = input("Noua mancare: ")
                pret_mancare_noua = float(input("Pret mancare noua: "))
                cantitate_mancare_noua = int(input("Cantitate mancare noua: "))
                durata_preparare_mancare_noua = int(input("Durata noua preparare: "))
                self.meniu.adaugare_mancare(Mancare(tip_mancare_noua,pret_mancare_noua,durata_preparare_mancare_noua,cantitate_mancare_noua))
                self.meniu.afis_mancare()
            #////
            elif optiune == 2:
                id = int(input("Introduceti ID-ul mancarii  pe care doriiti sa o modificati, daca nu doriti tastati Enter: "))
                tip_mancare_noua = input("Noua mancare: ")
                if tip_mancare_noua == '':
                    tip_mancare_noua = self.meniu.mancaruri_existente[id-1].tip_mancare
                pret_mancare_noua = input("Pret mancare noua: ")
                if pret_mancare_noua == '':
                    pret_mancare_noua = self.meniu.mancaruri_existente[id-1].pret
                cantitate_mancare_noua = input("Cantitate mancare noua: ")
                if cantitate_mancare_noua == '':
                    cantitate_mancare_noua = self.meniu.mancaruri_existente[id-1].gramaj
                durata_preparare_mancare_noua = input("Durata noua de preparare: ")
                if durata_preparare_mancare_noua == '':
                    durata_preparare_mancare_noua = self.meniu.mancaruri_existente[id-1].timp_preparare

                self.meniu.modificare_mancare(id,mancare_noua=tip_mancare_noua,pret_nou=float(pret_mancare_noua),cantitate_noua=int(cantitate_mancare_noua),timp_nou=int(durata_preparare_mancare_noua))
                self.meniu.afis_mancare()
            #////
            elif optiune == 3:
                id = int(input("Introduceti ID-ul mancarii  pe care doriiti sa o stergeti: "))
                self.meniu.stergere_mancare(id)
                self.meniu.afis_mancare()
            #////
            else:
                break

    def optiunea2(self):
        self.meniu.afis_bautura()
        while True:
            print('''

            Daca doriti sa faceti modificari aveti urmatoarele variante:

            1 - Adaugare element in meniul de bautura
            2 - Modificare element in meniul de bautura
            3 - Stergere element in meniul de bautura
            4 - Nu se efectueaza nicio operatie

            ''')

            optiune = int(input("Tastati optiunea: "))

            if optiune == 1:
                tip_bautura_noua = input("Noua bautura: ")
                pret_bautura_noua = float(input("Pret bautura noua: "))
                cantitate_alcool_noua = int(input("Cantitate alcool noua: "))
                self.meniu.adaugare_bautura(Bautura(tip_bautura_noua,pret_bautura_noua,cantitate_alcool_noua))
                self.meniu.afis_bautura()

            #////
            elif optiune == 2:
                id = int(input("Introduceti ID-ul bauturii  pe care doriiti sa o modificati, daca nu doriti tastati Enter: "))
                tip_bautura_noua = input("Noua bautura: ")
                if tip_bautura_noua == '':
                    tip_bautura_noua = self.meniu.bauturi_existente[id - 1].tip_bautura
                pret_bautura_noua = input("Pret bautura noua: ")
                if pret_bautura_noua == '':
                    pret_bautura_noua = self.meniu.bauturi_existente[id - 1].pret
                cantitate_alcool_noua = input("Cantitate alcool bautura noua: ")
                if cantitate_alcool_noua == '':
                    cantitate_alcool_noua = self.meniu.bauturi_existente[id - 1].cantitate_alcool

                self.meniu.modificare_bauturi(id,bautura_noua=tip_bautura_noua,pret_bautura_noua=float(pret_bautura_noua),cantitate_alcool_bautura_noua=int(cantitate_alcool_noua))
                self.meniu.afis_bautura()

            #////
            elif optiune == 3:
                id = int(input("Introduceti ID-ul mancarii  pe care doriiti sa o stergeti: "))
                self.meniu.stergere_bautura(id)
                self.meniu.afis_bautura()

            else:
                break

    def optiunea3(self):
        self.listaclienti.afisare_clienti()
        while True:
            print('''

            Daca doriti sa faceti modificari aveti urmatoarele variante:

            1 - Adaugare client nou
            2 - Modificare client existent
            3 - Stergere client
            4 - Cautare client
            5 - Nu se efectueaza nicio operatie

            ''')

            optiune = int(input("Tastati optiunea: "))
            if optiune == 1:
                nume_nou = input("Introduceti numele si prenumele clientului: ")
                adresa_noua = input("Introduceti adresa completa: ")
                self.listaclienti.adaugare_client(Client(nume_nou, adresa_noua))
                print("Client adaugat cu succes!")
            #////
            elif optiune == 2:
                self.listaclienti.afisare_clienti()
                id = int(input("Introduceti ID-ul clientului pe care doriti sa il modificati, daca nu doriti tastati Enter: "))
                nume_modificat = input("Introduceti numele nou al clientului: ")
                if nume_modificat == '':
                    nume_modificat = self.listaclienti[id-1].nume
                adresa_modificata = input("Introduceti adresa noua a clientului: ")
                if adresa_modificata == '':
                    adresa_modificata = self.listaclienti[id-1].adresa
                self.listaclienti.modificare_client(id,nume_client=nume_modificat,adresa_client=adresa_modificata)
            #////
            elif optiune == 3:
                id = int(input("Introduceti ID-ul clientului pe care doriti sa il stergeti: "))
                self.listaclienti.stergere_client(id)
            #////
            elif optiune == 4:
                secventa = input("Introduceti secventa de litere dupa care vrei sa cautati clientul,\n"
                                 "aceasta poate sa fie si nume si din adresa: ")
                lista_posibilitati = self.listaclienti.cautare_client(secventa)
                if not lista_posibilitati:"Nu exista niciun client dupa acest criteriu"
                else:
                    print('Rezultatele cautarii: ')
                    for index, client in enumerate(lista_posibilitati, start=1):
                        print(f"{index}. {client}")
            #////
            else:
                break

    def optiunea4(self):
        #decizie = input("Ce mancare doriti sa adaugati? Introduceti ID-ul acesteia, cand nu mai doriti sa adaugati mancare tastati '0': ")

        self.comanda.afisare_comanda()
        rezultat = self.comanda.verificare_existenta_client()
        if  rezultat == 0:
            print("Clientul nu vrea sa fie adaugat in baza de date: ")
            nume_provizoriu_comanda = input("Introduceti numele si prenumele clientului: ")
            adresa_provizorie_comanda = input("Introduceti adresa completa: ")
            client_ales = Client(nume_provizoriu_comanda,adresa_provizorie_comanda)
        else:
            lista_posibilitati = rezultat
            for index,client in enumerate(lista_posibilitati,start=1):
                print(f"{index}. Nume: {client.nume}, adresa: {client.adresa}\n")
            nr = int(input("Introduceti ID-ul din lista de rezultate: "))
            client_ales = lista_posibilitati[nr-1]
        print(f"{Fore.RED}/////////////////////////////////////////////////////////////////////////////////////////////////////////{Fore.RESET}")
        print(f"{Fore.YELLOW}---------------------------------------------SUMAR COMANDA-----------------------------------------------{Fore.RESET}")
        print(f"{Fore.GREEN}Comanda contine urmatorele feluri de mancare: {Fore.RESET}")
        # print(self.comanda.lista_comanda_mancare)
        for mancare in self.comanda.lista_comanda_mancare:
            print(f"-->{mancare}")
        print(f"{Fore.GREEN}Comanda contine urmatoarele bauturi: {Fore.RESET}")
        # print(self.comanda.lista_comanda_bauturi)
        for bautura in self.comanda.lista_comanda_bauturi:
            print(f"-->{bautura}")
        print(f"Comanda s-a efectuat pe numele {Fore.MAGENTA}{client_ales.nume}{Fore.RESET} si se va livra la adresa {Fore.CYAN}{client_ales.adresa}{Fore.RESET}")
        self.comanda.calculare_comanda()
        print(f"{Fore.RED}/////////////////////////////////////////////////////////////////////////////////////////////////////////{Fore.RESET}")







    def opt123(self):
        print('''

                    Bun venit, ce doriti sa faceti?

                    1 - Vizualizare meniu mancare + modificare meniu mancare 
                    2 - Vizualizare meniu bautura + modificare meniu bautura
                    3 - Vizualizare clienti + modificare lista clienti
                    4 - Creare comanda noua

        ''')


    def alegere_optiuni(self):

        while True:
            self.opt123()
            optiune = int(input("Tastati opitunea: "))
            if optiune == 1:
                self.optiunea1()
            elif optiune == 2:
                self.optiunea2()
            elif optiune == 3:
                self.optiunea3()
            elif optiune == 4:
                self.optiunea4()
            else: break
