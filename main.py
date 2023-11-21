from Databasecontroller import DatabaseController
from Speler import Speler
from MatchStats import MatchStats

def main():
    db_controller = DatabaseController()

    while True:
        print("\n1. Voeg speler toe")
        print("2. Toon alle spelers")
        print("3. Voeg matchstatistieken toe")
        print("4. Bewerk speler")
        print("5. Verwijder speler")
        print("6. Toon matchstatistieken van speler")
        print("7. Toon alle statistieken van match")
        print("8. Sluit programma")

        keuze = input("Voer het nummer van uw keuze in: ")

        if keuze == "1":
            voornaam = input("Voornaam: ")
            familienaam = input("Familienaam: ")
            nummer = int(input("Nummer: "))
            nieuwe_speler = Speler(voornaam, familienaam, nummer)
            db_controller.insert_speler(nieuwe_speler)
            print("Speler toegevoegd.")

        elif keuze == "2":
            spelers = db_controller.get_all_spelers()
            print("\nAlle spelers:")
            for speler in spelers:
                print(speler)

        elif keuze == "3":
            speler_id = int(input("Speler ID: "))
            matchnummer = int(input("Matchnummer: "))
            gespeelde_minuten = int(input("Aantal gespeelde minuten: "))
            gescoorde_punten = int(input("Aantal gescoorde punten: "))
            nieuwe_matchstats = MatchStats(speler_id, matchnummer, gespeelde_minuten, gescoorde_punten)
            db_controller.insert_matchstats(nieuwe_matchstats)
            print("Matchstatistieken toegevoegd.")

        elif keuze == "4":
            speler_id = int(input("Speler ID: "))
            voornaam = input("Nieuwe voornaam: ")
            familienaam = input("Nieuwe familienaam: ")
            nummer = int(input("Nieuw nummer: "))
            bewerkte_speler = Speler(voornaam, familienaam, nummer)
            db_controller.update_speler(speler_id, bewerkte_speler)
            print("Speler bewerkt.")

        elif keuze == "5":
            speler_id = int(input("Speler ID: "))
            db_controller.delete_speler(speler_id)
            print("Speler verwijderd.")

        elif keuze == "6":
            speler_id = int(input("Speler ID: "))
            matchstatistieken = db_controller.get_matchstats_van_speler(speler_id)
            print(f"\nMatchstatistieken van speler {speler_id}:")
            for stat in matchstatistieken:
                print(stat)

        elif keuze == "7":
            matchnummer = int(input("Matchnummer: "))
            matchstatistieken = db_controller.get_matchstats_van_match(matchnummer)
            print(f"\nAlle statistieken van match {matchnummer}:")
            for stat in matchstatistieken:
                print(stat)

        elif keuze == "8":
            print("Programma wordt afgesloten.")
            break

        else:
            print("Ongeldige keuze. Probeer opnieuw.")

    db_controller.close_connection()

if __name__ == "__main__":
    main()