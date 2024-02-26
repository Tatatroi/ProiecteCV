import pickle
class ListaClienti:
    # f = open("clienti.pck",'rb')
    # lista_clienti = pickle.load(f)
    # f.close()

    def __init__(self):
        self.incarca_date()
    def afisare_clienti(self):
        print('Clienti inregistrati in magazin')
        for index, client in enumerate(self.lista_clienti, start=1):
            print(f"{index}. Nume: {client.nume}, adresa: {client.adresa}")


    def incarca_date(self):
        with open("clienti.pck",'rb')as f:
            self.lista_clienti = pickle.load(f)

    def salvare_cient(self):
        with open("clienti.pck", 'wb') as f:
            pickle.dump(self.lista_clienti,f)


    def adaugare_client(self, client_nou: "Client"):
        if isinstance(client_nou,Client):
            self.lista_clienti.append(client_nou)
            print(f"Clientul {client_nou.nume} a fost adaugat!")
            self.salvare_cient()
            self.incarca_date()
            self.afisare_clienti()
        else:
            return "Eroare! Obiectul trebuie sa fie de tipul client!"

    def cautare_client(self, secventa:str):
        lista_posibilitati = []
        for client in self.lista_clienti:
            if secventa.lower() in client.nume.lower() or secventa.lower() in client.adresa.lower():
                lista_posibilitati.append(client)
        return lista_posibilitati

    def stergere_client(self,id_client):
        if 1 <= id_client <= len(self.lista_clienti):
            self.lista_clienti.pop(id_client-1)
            print("Clientul s-a sters cu succes!")
            self.salvare_cient()
            self.incarca_date()
            self.afisare_clienti()
        else:
            return f"Clientul cu ID - ul {id_client} nu exista!"

    def modificare_client(self, id, nume_client = None, adresa_client = None):
        if 1 <= id <= len(self.lista_clienti):
            if nume_client is not None:
                self.lista_clienti[id-1].nume = nume_client
            if adresa_client is not None:
                self.lista_clienti[id-1].adresa = adresa_client
            self.salvare_cient()
            self.incarca_date()
            self.afisare_clienti()
        else:
            return f"Clientul cu ID-ul {id} nu exista, trebuie adaugat!"






class Client:
    def __init__(self,nume,adresa):
        self.nume = nume
        self.adresa = adresa

    def __str__(self):
        return f"Nume client: {self.nume}\n Adresa client: {self.adresa}\n\n"

    def __eq__(self, other):
        if isinstance(other,Client):
            return self.nume.lower() == other.nume.lower() and self.adresa.lower() == other.adresa.lower()
