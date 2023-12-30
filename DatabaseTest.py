import unittest
from Controllers.Databasecontroller import DatabaseController
from Models.Speler import Speler
from Models.MatchStats import MatchStats
import os

class TestDatabaseController(unittest.TestCase):
    def setUp(self):
        self.test_db_name = "test_spelers.db"
        self.db_controller = DatabaseController(database_name=self.test_db_name)

    def tearDown(self):
        self.db_controller.close_connection()
        if os.path.exists(self.test_db_name):
            os.remove(self.test_db_name)

    def test_insert_and_get_speler(self):
        test_speler = Speler("John", "Doe", 1)
        self.db_controller.insert_speler(test_speler)

        result = self.db_controller.get_all_spelers()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], test_speler.to_tuple())

    def test_update_speler(self):
        test_speler = Speler("John", "Doe", 1)
        self.db_controller.insert_speler(test_speler)

        updated_speler = Speler("Karel", "Doe", 1)
        self.db_controller.update_speler(1, updated_speler)

        result = self.db_controller.get_all_spelers()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], updated_speler.to_tuple())

    def test_delete_speler(self):
        test_speler = Speler("John", "Doe", 1)
        self.db_controller.insert_speler(test_speler)

        self.db_controller.delete_speler(1)

        result = self.db_controller.get_all_spelers()
        self.assertEqual(len(result), 0)

    def test_insert_and_get_matchstats(self):
        test_matchstats = MatchStats(1, 1, 30, 15)
        self.db_controller.insert_matchstats(test_matchstats)

        result = self.db_controller.get_matchstats_van_speler(1)

        self.assertGreaterEqual(len(result), 1)
        self.assertEqual(result[0][1:], test_matchstats.to_tuple())
    
    def test_get_all_matchstats(self):
        test_matchstats1 = MatchStats(1, 1, 30, 15)
        test_matchstats2 = MatchStats(2, 1, 25, 10)

        self.db_controller.insert_matchstats(test_matchstats1)
        self.db_controller.insert_matchstats(test_matchstats2)

        result = self.db_controller.get_all_matchstats()

        self.assertGreaterEqual(len(result), 1)
        self.assertEqual(result[0][1:], test_matchstats1.to_tuple())
        self.assertEqual(result[1][1:], test_matchstats2.to_tuple())

if __name__ == "__main__":
    unittest.main()
