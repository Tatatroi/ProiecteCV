import pickle
from REPOSITORY.repository import Meniu
from REPOSITORY.repository import Mancare
from REPOSITORY.repository import Bautura
from REPOSITORY.repositoryclient import ListaClienti,Client
from UI.ui import Ui
from CONTROLLER.controller import Comanda
from TESTS.teste import Teste
def main():
    # mancaruri_existente = [Mancare("Salata",12.50,10,350)]
    # bauturi_existente = [Bautura("Cola",8.00,0)]
    #
    # with open("meniumancare.pck", 'wb') as f:
    #     pickle.dump(mancaruri_existente, f)
    #
    # with open("meniubauturi.pck", 'wb') as f:
    #     pickle.dump(bauturi_existente, f)

    # meniu1 = Meniu()
    #
    # meniu1.adaugare_mancare(Mancare("Salata",12.50,10,350))
    # meniu1.adaugare_mancare(Mancare("Cartofi pai",20,15,450))
    # meniu1.adaugare_mancare(Mancare("Paste Carbonara",38.99,30,550))
    #
    #
    # meniu1.modificare_mancare(2,mancare_noua="Cartofi copti",pret_nou=40,cantitate_noua=500)
    # #meniu1.stergere_mancare(6)
    #
    # meniu1.modificare_mancare(5,mancare_noua="pizza",pret_nou=50)
    # # meniu1.afis_mancare(meniu1)
    #
    # #meniu1.adaugare_bautura(Bautura("Pepsi",10,0))
    # #meniu1.adaugare_bautura(Bautura("Whiskey",100,30))
    # meniu1.modificare_bauturi(1,bautura_noua="Sprite",pret_bautura_noua=10)
    #
    # meniu1.afis_mancare()
    #
    #
    # meniu1.afis_bautura()


    # listaClienti = [Client("Mitori Stefan","Calea Floresti nr. 58b")]
    #
    # with open("clienti.pck",'wb') as f:
    #     pickle.dump(listaClienti,f)

    teste = Teste()
    teste.test_adaugare_mancare_succes()
    teste.test_adaugare_mancare_existenta()
    teste.test_cautare_client()


    meniu1= Meniu()
    lista_clienti = []
    lista_clienti = ListaClienti()
    comanda = Comanda(meniu1,lista_clienti)
    ui = Ui(meniu1,lista_clienti,comanda)
    ui.alegere_optiuni()

main()