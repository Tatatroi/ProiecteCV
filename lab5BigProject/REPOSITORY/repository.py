import pickle

class Meniu:

    def __init__(self):
        self.incarca_date()

    # def incarca_date(self):
    #     try:
    #         with open("meniumancare.pck", 'rb') as f:
    #             self.mancaruri_existente = pickle.load(f)
    #     except (EOFError, FileNotFoundError):
    #         self.mancaruri_existente = []
    #
    #     try:
    #         with open("meniubauturi.pck", 'rb') as f:
    #             self.bauturi_existente = pickle.load(f)
    #     except (EOFError, FileNotFoundError):
    #         self.bauturi_existente = []

    def incarca_date(self):
        with open("meniumancare.pck",'rb')as f:
            self.mancaruri_existente = pickle.load(f)

        with open("meniubauturi.pck",'rb') as f:
            self.bauturi_existente = pickle.load(f)

    # f = open("meniumancare.pck",'rb')
    # mancaruri_existente = pickle.load(f)
    # f.close()
    # f = open("meniubauturi.pck",'rb')
    # bauturi_existente = pickle.load(f)
    # f.close()

    def salvare_mancare(self):
        with open("meniumancare.pck", 'wb') as f:
            pickle.dump(self.mancaruri_existente, f)

    def salvare_bauturi(self):
        with open("meniubauturi.pck", 'wb') as f:
            pickle.dump(self.bauturi_existente, f)


    #Functie afisare mancare disponibila
    def afis_mancare(self):
        print('Mancaruri disponibile: ')
        for index, mancare in enumerate(self.mancaruri_existente, start=1):
            print(f"{index}. {mancare}")

    def adaugare_mancare(self, mancare_noua: "Mancare"):
        if mancare_noua in self.mancaruri_existente:
            return "Aceasta mancare exista deja!"
        self.mancaruri_existente.append(mancare_noua)
        print("Noua mancare s-a adaugat cu succes!")

        self.salvare_mancare()
        self.incarca_date()

    # Functia de adaugare de mai jos se foloseste doar penntru teste ca sa nu adauge in fisierele pickle,
    # este ca si cea originiala doar ca nu apeleaza functiile de salvare si incarcare date
    def adaugare_mancare_test(self, mancare_noua: "Mancare"):
        if mancare_noua in self.mancaruri_existente:
            return "Aceasta mancare exista deja!"
        self.mancaruri_existente.append(mancare_noua)

    def modificare_mancare(self, id, mancare_noua = None, pret_nou = None, cantitate_noua = None, timp_nou = None):
        if 1 <= id <= len(self.mancaruri_existente):
            if mancare_noua is not None:
                self.mancaruri_existente[id - 1].tip_mancare = mancare_noua
            if pret_nou is not None:
                self.mancaruri_existente[id - 1].pret = pret_nou
            if cantitate_noua is not None:
                self.mancaruri_existente[id - 1].gramaj = cantitate_noua
            if timp_nou is not None:
                self.mancaruri_existente[id - 1].timp_preparare = timp_nou
            print("Modificarea s-a efectuat cu succes!")
            self.salvare_mancare()
            self.incarca_date()

        else:
            return "ID-ul specificat nu exista in lista de mancaruri."

    def stergere_mancare(self,id:int):
        if 1 <= id <= len(self.mancaruri_existente):
            self.mancaruri_existente.pop(id-1)
            print("Mancare stearsa cu succes!")
            self.salvare_mancare()
            self.incarca_date()
        else:
            return "ID-ul specificat nu exista in lista de mancaruri."


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # Functie afisare bautura disponibila
    def afis_bautura(self):
        print("Bauturi disponibile: ")
        for index, bautura in enumerate(self.bauturi_existente, start=1):
            print(f"{index}. {bautura}")

    #Functie pentru adaugare bauturi noi
    def adaugare_bautura(self,bautura_noua: "Bautura"):
        if bautura_noua in self.bauturi_existente:
            return "Aceasta bautura exista deja!"
        self.bauturi_existente.append(bautura_noua)
        self.salvare_bauturi()
        self.incarca_date()


    def modificare_bauturi(self,id: int,bautura_noua = None, pret_bautura_noua = None, cantitate_alcool_bautura_noua = None):
        if 1 <= id <= len(self.bauturi_existente):
            if bautura_noua is not None:
                self.bauturi_existente[id-1].tip_bautura = bautura_noua
            if pret_bautura_noua is not None:
                self.bauturi_existente[id-1].pret_bautura = pret_bautura_noua
            if cantitate_alcool_bautura_noua is not None:
                self.bauturi_existente[id-1].cantitate_alcool = cantitate_alcool_bautura_noua
            print("Modificarea s-a efectuat cu succes!")
            self.salvare_bauturi()
            self.incarca_date()

        else:
            return "ID-ul specificat nu exista in lista de bauturi."

    def stergere_bautura(self, id: int):
        if 1 <= id <= len(self.bauturi_existente):
            self.bauturi_existente.pop(id-1)
            print("Bautura stearsa cu succes!")
            self.salvare_bauturi()
            self.incarca_date()

        else:
            return "ID-ul specificat nu exista in lista de bauturi."

class Mancare:
    def __init__(self,tip_mancare: str,pret: float,timp_preparare: int,gramaj: int):
        self.tip_mancare = tip_mancare
        self.pret = pret
        self.timp_preparare = timp_preparare
        self.gramaj = gramaj

    def __str__(self):
        return f"{self.tip_mancare}, {self.pret} lei, {self.timp_preparare} minute, gramaj: {self.gramaj} g"

    def __eq__(self, other):
        if isinstance(other,Mancare):
            return self.tip_mancare == other.tip_mancare and self.pret == other.pret and self.timp_preparare == other.timp_preparare and self.gramaj == other.gramaj

class Bautura:

    def __init__(self,tip_bautura: str, pret: float, cantitate_alcool: int):
        self.tip_bautura = tip_bautura
        self.pret = pret
        self.cantitate_alcool = cantitate_alcool

    def __str__(self):
        return f"{self.tip_bautura}, {self.pret} lei, alcool: {self.cantitate_alcool}%"

    def __eq__(self, other):
        if isinstance(other,Bautura):
            return self.tip_bautura.lower == other.tip_bautura.lower() and self.pret == other.pret and self.cantitate_alcool == other.cantitate_alcool
        return False