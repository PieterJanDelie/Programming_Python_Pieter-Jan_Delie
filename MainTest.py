import unittest
from unittest.mock import patch
from main import (
    voeg_speler_toe,
    toon_alle_spelers,
    voeg_matchstatistieken_toe,
    bewerk_speler,
    verwijder_speler,
    toon_matchstatistieken_van_speler,
    toon_alle_statistieken_van_match,
    schrijf_naar_csv_of_excel
)


class TestMainFunctions(unittest.TestCase):

    @patch("builtins.input", side_effect=["John", "Doe", "42"])
    def test_voeg_speler_toe(self, mock_input):
        db_controller_mock = unittest.mock.MagicMock()
        voeg_speler_toe(db_controller_mock)
        db_controller_mock.insert_speler.assert_called_once()

    @patch("builtins.input", side_effect=["1"])
    def test_toon_alle_spelers(self, mock_input):
        db_controller_mock = unittest.mock.MagicMock()
        toon_alle_spelers(db_controller_mock)
        db_controller_mock.get_all_spelers.assert_called_once()

    @patch("builtins.input", side_effect=["1", "1", "10", "20"])
    def test_voeg_matchstatistieken_toe(self, mock_input):
        db_controller_mock = unittest.mock.MagicMock()
        voeg_matchstatistieken_toe(db_controller_mock)
        db_controller_mock.insert_matchstats.assert_called_once()

    @patch("builtins.input", side_effect=["1", "John", "Doe", "42"])
    def test_bewerk_speler(self, mock_input):
        db_controller_mock = unittest.mock.MagicMock()
        bewerk_speler(db_controller_mock)
        db_controller_mock.update_speler.assert_called_once()

    @patch("builtins.input", side_effect=["1"])
    def test_verwijder_speler(self, mock_input):
        db_controller_mock = unittest.mock.MagicMock()
        verwijder_speler(db_controller_mock)
        db_controller_mock.delete_speler.assert_called_once()

    @patch("builtins.input", side_effect=["1"])
    def test_toon_matchstatistieken_van_speler(self, mock_input):
        db_controller_mock = unittest.mock.MagicMock()
        toon_matchstatistieken_van_speler(db_controller_mock)
        db_controller_mock.get_matchstats_van_speler.assert_called_once()

    @patch("builtins.input", side_effect=["1"])
    def test_toon_alle_statistieken_van_match(self, mock_input):
        db_controller_mock = unittest.mock.MagicMock()
        toon_alle_statistieken_van_match(db_controller_mock)
        db_controller_mock.get_matchstats_van_match.assert_called_once()

    @patch("builtins.input", side_effect=["csv"])
    def test_schrijf_naar_csv_of_excel_csv(self, mock_input):
        db_controller_mock = unittest.mock.MagicMock()
        schrijf_naar_csv_of_excel(db_controller_mock)
        db_controller_mock.get_all_spelers.assert_called_once()
        db_controller_mock.get_all_matchstats.assert_called_once()
        
    @patch("builtins.input", side_effect=["excel"])
    def test_schrijf_naar_csv_of_excel_excel(self, mock_input):
        db_controller_mock = unittest.mock.MagicMock()
        schrijf_naar_csv_of_excel(db_controller_mock)
        db_controller_mock.get_all_spelers.assert_called_once()
        db_controller_mock.get_all_matchstats.assert_called_once()
        
if __name__ == '__main__':
    unittest.main()
