from Persoon import Persoon;
from databasecontroller import DatabaseController;

def startProgram():
    db_controller.maak_tabel_indien_nodig()
    choice = ""
    while (choice != "e"):
        choice = input("Wat wil je doen (v) verjaardagen bekijken, (i) ingeven van een verjaardag, (e) beïndig het programma: ")
        match choice:
            case "v":
                bekijkverjaardagen()
            case "i":
                ingevenverjaardag()
            case"e":
                print("Bedankt om deze tool te gebruiken")

def bekijkverjaardagen():
	druk_alle_personen_af(db_controller.haal_personen_op())

def druk_alle_personen_af(personen):
    for persoon in personen:
        print(f"Voornaam: {persoon[1]}")
        print(f"Achternaam: {persoon[2]}")
        print(f"Geboortedatum: {persoon[3]}")
        print("----------------------")

def ingevenverjaardag():
	db_controller.voeg_persoon_toe_aan_database(maak_persoon_aan())

def maak_persoon_aan():
    """voornaam = input("Voer de voornaam in: ")
    achternaam = input("Voer de achternaam in: ")
    geboortedatum = input("Voer de geboortedatum in: ")
    aanspreking = input("Voer de aanspreking in: ")

    persoon = Persoon(voornaam, achternaam, geboortedatum, aanspreking)"""
    persoon = Persoon("Lars", "Buyck","07/11/2002", "Maatje")
    return persoon


if __name__ == "__main__":
    db_controller = DatabaseController()
    startProgram()

