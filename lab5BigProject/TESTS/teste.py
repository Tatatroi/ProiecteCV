from REPOSITORY.repository import Meniu, Mancare
from REPOSITORY.repositoryclient import Client,ListaClienti
class Teste:

    def test_adaugare_mancare_succes(self):
        meniu_test = Meniu()
        mancare_noua = Mancare("Peste", 20, 15, 280)

        result = meniu_test.adaugare_mancare_test(mancare_noua)

        assert result is None, f"Rezultat așteptat: None, Rezultat obținut: {result}"
        assert mancare_noua in meniu_test.mancaruri_existente, f"Mancarea {mancare_noua} nu a fost adăugată în lista"

    def test_adaugare_mancare_existenta(self):
        meniu_test = Meniu()
        mancare_existenta = Mancare("Peste", 20, 15, 280)
        meniu_test.mancaruri_existente.append(mancare_existenta)

        result = meniu_test.adaugare_mancare_test(mancare_existenta)

        assert result == "Aceasta mancare exista deja!", f"Rezultat așteptat: 'Aceasta mancare exista deja!', Rezultat obținut: {result}"
        assert meniu_test.mancaruri_existente.count(mancare_existenta) == 1, f"Mancarea {mancare_existenta} a fost adăugată în lista de mai multe ori"

    def test_cautare_client(self):
        lista_clienti_test = ListaClienti()
        client1 = Client("John Doe", "Strada Primaverii")
        client2 = Client("Jane Doe", "Strada Crangului")
        client3 = Client("Alex Smith", "Bulevardul Independentei")
        lista_clienti_test.lista_clienti = [client1, client2, client3]

        # Test pentru căutare cuvânt cheie în nume
        rezultat_nume = lista_clienti_test.cautare_client("Doe")
        assert len(rezultat_nume) == 2, f"Numărul așteptat de rezultate: 2, Numărul obținut: {len(rezultat_nume)}"

        # Verificăm dacă clienții returnați sunt cei așteptați
        assert client1 in rezultat_nume, "Clientul așteptat nu a fost găsit în rezultate"
        assert client2 in rezultat_nume, "Clientul așteptat nu a fost găsit în rezultate"

        # Test pentru căutare cuvânt cheie în adresa
        rezultat_adresa = lista_clienti_test.cautare_client("Independentei")
        assert len(rezultat_adresa) == 1, f"Numărul așteptat de rezultate: 1, Numărul obținut: {len(rezultat_adresa)}"

        # Verificăm dacă clientul returnat este cel așteptat
        assert client3 in rezultat_adresa, "Clientul așteptat nu a fost găsit în rezultate"

    # def test_modificare_nume_client(self):
    #     lista_clienti_test = ListaClienti()
    #     client_initial = Client("John Doe", "Strada Primaverii")
    #     lista_clienti_test.lista_clienti = [client_initial]
    #
    #     # Testăm modificarea numelui clientului
    #     lista_clienti_test.modificare_client(1, nume_client="Jane Doe")
    #
    #     # Verificăm dacă modificarea s-a făcut corect
    #     client_modificat = lista_clienti_test.lista_clienti[0]
    #     assert client_modificat.nume == "Jane Doe", f"Numele așteptat: 'Jane Doe', Nume obținut: {client_modificat.nume}"
    #
    # def test_modificare_adresa_client(self):
    #     lista_clienti_test = ListaClienti()
    #     client_initial = Client("John Doe", "Strada Primaverii")
    #     lista_clienti_test.lista_clienti = [client_initial]
    #
    #     # Testăm modificarea adresei clientului
    #     lista_clienti_test.modificare_client(1, adresa_client="Strada Crangului")
    #
    #     # Verificăm dacă modificarea s-a făcut corect
    #     client_modificat = lista_clienti_test.lista_clienti[0]
    #     assert client_modificat.adresa == "Strada Crangului", f"Adresa așteptată: 'Strada Crangului', Adresa obținută: {client_modificat.adresa}"



