import sqlite3
from Speler import Speler
from MatchStats import MatchStats

class DatabaseController:
    def __init__(self, database_name="spelers.db"):
        self.conn = sqlite3.connect(database_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS spelers (
                nummer INTEGER PRIMARY KEY,
                voornaam TEXT,
                familienaam TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS matchstats (
                id INTEGER PRIMARY KEY,
                speler_nummer INTEGER,
                matchnummer INTEGER,
                gespeelde_minuten INTEGER,
                gescoorde_punten INTEGER,
                FOREIGN KEY (speler_nummer) REFERENCES spelers (nummer)
            )
        ''')

        self.conn.commit()

    def insert_speler(self, speler):
        if not isinstance(speler, Speler):
            raise ValueError("Verwacht een instantie van de Speler-klasse")

        if self.check_nummer_exists(speler.nummer):
            print(f"Speler met nummer {speler.nummer} bestaat al.")
            return

        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO spelers (nummer, voornaam, familienaam)
            VALUES (?, ?, ?)
        ''', speler.to_tuple())
        self.conn.commit()

    def update_speler(self, speler_id, speler):
        if not isinstance(speler, Speler):
            raise ValueError("Verwacht een instantie van de Speler-klasse")

        if self.check_nummer_exists(speler.nummer, exclude_speler_id=speler_id):
            print(f"Speler met nummer {speler.nummer} bestaat al.")
            return

        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                UPDATE spelers
                SET voornaam=?, familienaam=?, nummer=?
                WHERE nummer=?
            ''', (speler.voornaam, speler.familienaam, speler.nummer, speler_id))
            self.conn.commit()
        except sqlite3.Error as e:
            print("SQLite error:", e)
            raise e

    def delete_speler(self, speler_id):
        cursor = self.conn.cursor()
        cursor.execute('''
            DELETE FROM spelers
            WHERE nummer=?
        ''', (speler_id,))
        self.conn.commit()

    def get_all_spelers(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM spelers
        ''')
        return cursor.fetchall()

    def insert_matchstats(self, matchstats):
        if not isinstance(matchstats, MatchStats):
            raise ValueError("Verwacht een instantie van de MatchStats-klasse")

        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO matchstats (speler_nummer, matchnummer, gespeelde_minuten, gescoorde_punten)
            VALUES (?, ?, ?, ?)
        ''', matchstats.to_tuple())
        self.conn.commit()

    def get_matchstats_van_speler(self, speler_id):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM matchstats
            WHERE speler_nummer=?
        ''', (speler_id,))
        return cursor.fetchall()

    def get_matchstats_van_match(self, matchnummer):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM matchstats
            WHERE matchnummer=?
        ''', (matchnummer,))
        return cursor.fetchall()

    def close_connection(self):
        self.conn.close()

    def check_nummer_exists(self, nummer, exclude_speler_id=None):
        cursor = self.conn.cursor()
        if exclude_speler_id is not None:
            cursor.execute('''
                SELECT COUNT(*) FROM spelers WHERE nummer=? AND nummer<>?
            ''', (nummer, exclude_speler_id))
        else:
            cursor.execute('''
                SELECT COUNT(*) FROM spelers WHERE nummer=?
            ''', (nummer,))

        result = cursor.fetchone()
        return result[0] > 0
