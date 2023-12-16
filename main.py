import pandas as pd
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
        statMatchStat = MatchStats.from_tuple(stat)
        print(statMatchStat)

def toon_alle_statistieken_van_match(db_controller):
    matchnummer = int(input("Matchnummer: "))
    matchstatistieken = db_controller.get_matchstats_van_match(matchnummer)
    print(f"\nAlle statistieken van match {matchnummer}:")
    for stat in matchstatistieken:
        print(stat)


def schrijf_naar_csv_of_excel(db_controller):
    print("Wil je de gegevens wegschrijven naar een CSV- of Excel-bestand?")
    keuze = input("Voer 'csv' of 'excel' in: ").lower()

    if keuze not in ['csv', 'excel']:
        print("Ongeldige keuze. Probeer opnieuw.")
        schrijf_naar_csv_of_excel(db_controller)
        return

    spelers_data = db_controller.get_all_spelers()
    matchstats_data = db_controller.get_all_matchstats()

    spelers_df = pd.DataFrame(spelers_data, columns=["Nummer", "Voornaam", "Familienaam"])
    matchstats_df = pd.DataFrame(matchstats_data, columns=["ID", "Speler_Nummer", "Match_Nummer", "Gespeelde_Minuten", "Gescoorde_Punten"])

    gemiddelde_per_speler = matchstats_df.groupby("Speler_Nummer").mean()[["Gespeelde_Minuten", "Gescoorde_Punten"]]

    spelers_df = pd.merge(spelers_df, gemiddelde_per_speler, left_on="Nummer", right_index=True, how="left", suffixes=("", "_Gemiddeld"))

    if keuze == 'csv':
        bestand_naam = "gegevens.csv"
        spelers_df.to_csv(bestand_naam, index=False)
        print(f"Gegevens zijn naar {bestand_naam} geschreven.")
    elif keuze == 'excel':
        bestand_naam = "gegevens.xlsx"
        spelers_df.to_excel(bestand_naam, index=False)
        print(f"Gegevens zijn naar {bestand_naam} geschreven.")

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
        print("8. Schrijf gemiddeldes naar extern bestand")
        print("9. Sluit programma")

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
                schrijf_naar_csv_of_excel(db_controller)

            case "9":
                print("Programma wordt afgesloten.")
                blijvenUitvoeren = False

            case _:
                print("Ongeldige keuze. Probeer opnieuw.")

    db_controller.close_connection()

if __name__ == "__main__":
    main()
