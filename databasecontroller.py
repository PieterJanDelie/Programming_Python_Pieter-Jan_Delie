import sqlite3
from datetime import datetime

class DatabaseController:
    def __init__(self, database_name='personen.db'):
        self.database_name = database_name

    def maak_tabel_indien_nodig(self):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS personen
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            voornaam TEXT,
            achternaam TEXT,
            geboortedatum TEXT,
            aanspreking TEXT)
        ''')

        connection.commit()
        connection.close()

    def haal_personen_op(self):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute('''SELECT * FROM personen''')
        personen = cursor.fetchall()

        connection.close()
        return personen

    def voeg_persoon_toe_aan_database(self, persoon):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()

        cursor.execute('''
            INSERT INTO personen (voornaam, achternaam, geboortedatum, aanspreking)
            VALUES (?, ?, ?, ?)''', (persoon.voornaam, persoon.achternaam, persoon.geboortedatum, persoon.aanspreking))

        connection.commit()
        connection.close()

    def haal_jarige_personen_op():
        vandaag = datetime.now().strftime('%m-%d')
        connection = sqlite3.connect('personen.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM personen WHERE strftime('%m-%d', geboortedatum) = ?", (vandaag,))
        jarige_personen = cursor.fetchall()

        connection.close()
        return jarige_personen

    def verwijder_alle_personen():
        connection = sqlite3.connect('personen.db')
        cursor = connection.cursor()

        cursor.execute('''DELETE FROM personen''')

        connection.commit()
        connection.close()
        