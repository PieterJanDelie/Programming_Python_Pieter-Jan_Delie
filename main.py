from Databasecontroller import DatabaseController
from Speler import Speler
from MatchStats import MatchStats

def __vraag_speler_id__():
    return int(input("Spelers-nummer: "))

def __spelerAanmakenViaConsole__():
    voornaam = input("Voornaam: ")
    familienaam = input("Familienaam: ")
    nummer = int(input("Nummer: "))
    nieuwe_speler = Speler(voornaam, familienaam, nummer)
    return nieuwe_speler

def voeg_speler_toe(db_controller):
    nieuwe_speler = __spelerAanmakenViaConsole__()
    db_controller.insert_speler(nieuwe_speler)

def toon_alle_spelers(db_controller):
    spelers = db_controller.get_all_spelers()
    print("\nAlle spelers:")
    for speler in spelers:
        print(speler)

def voeg_matchstatistieken_toe(db_controller):
    speler_id = __vraag_speler_id__()
    matchnummer = int(input("Matchnummer: "))
    gespeelde_minuten = int(input("Aantal gespeelde minuten: "))
    gescoorde_punten = int(input("Aantal gescoorde punten: "))
    nieuwe_matchstats = MatchStats(speler_id, matchnummer, gespeelde_minuten, gescoorde_punten)
    db_controller.insert_matchstats(nieuwe_matchstats)
    print("Matchstatistieken toegevoegd.")

def bewerk_speler(db_controller):
    speler_id = __vraag_speler_id__()
    bewerkte_speler = __spelerAanmakenViaConsole__()
    db_controller.update_speler(speler_id, bewerkte_speler)
    print("Speler bewerkt.")

def verwijder_speler(db_controller):
    speler_id = __vraag_speler_id__()
    db_controller.delete_speler(speler_id)
    print("Speler verwijderd.")

def toon_matchstatistieken_van_speler(db_controller):
    speler_id = __vraag_speler_id__()
    matchstatistieken = db_controller.get_matchstats_van_speler(speler_id)
    print(f"\nMatchstatistieken van speler {speler_id}:")
    for stat in matchstatistieken:
        statMatchStat = MatchStats(stat)
        print(statMatchStat)

def toon_alle_statistieken_van_match(db_controller):
    matchnummer = int(input("Matchnummer: "))
    matchstatistieken = db_controller.get_matchstats_van_match(matchnummer)
    print(f"\nAlle statistieken van match {matchnummer}:")
    for stat in matchstatistieken:
        print(stat)

def main():
    db_controller = DatabaseController()

    blijvenUitvoeren = True

    while blijvenUitvoeren:
        print("\n1. Voeg speler toe")
        print("2. Toon alle spelers")
        print("3. Voeg matchstatistieken toe")
        print("4. Bewerk speler")
        print("5. Verwijder speler")
        print("6. Toon matchstatistieken van speler")
        print("7. Toon alle statistieken van match")
        print("8. Sluit programma")

        keuze = input("Voer het nummer van uw keuze in: ")

        match keuze:
            case "1":
                voeg_speler_toe(db_controller)

            case "2":
                toon_alle_spelers(db_controller)

            case "3":
                voeg_matchstatistieken_toe(db_controller)

            case "4":
                bewerk_speler(db_controller)

            case "5":
                verwijder_speler(db_controller)

            case "6":
                toon_matchstatistieken_van_speler(db_controller)

            case "7":
                toon_alle_statistieken_van_match(db_controller)

            case "8":
                print("Programma wordt afgesloten.")
                blijvenUitvoeren = False

            case _:
                print("Ongeldige keuze. Probeer opnieuw.")

    db_controller.close_connection()

if __name__ == "__main__":
    main()
