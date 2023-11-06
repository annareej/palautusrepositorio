import unittest
from player import Player
from statistics_service import StatisticsService
from statistics_service import SortBy


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_pelaaja_loytyy(self):
        pelaaja = self.stats.search("Kurri")
        self.assertAlmostEqual(pelaaja.name, "Kurri")

    def test_search_pelaaja_ei_loydy(self):
        pelaaja = self.stats.search("Sandstrom")
        self.assertIsNone(pelaaja)

    def test_etsi_joukkue(self):
        odotettu_lista = ["Semenko", "Kurri", "Gretzky"]
        pelaajat = self.stats.team("EDM")
        nimet = []
        for pelaaja in pelaajat:
            nimet.append(pelaaja.name)

        self.assertEqual(odotettu_lista, nimet)

    def test_top(self):
        pelaaja = self.stats.top(1)[0]
        self.assertAlmostEqual(pelaaja.name, "Gretzky")

    def test_parhaat_pisteet(self):
        pelaaja = self.stats.top(1, SortBy.POINTS)[0]
        self.assertAlmostEqual(pelaaja.name, "Gretzky")
    
    def test_eniten_maaleja(self):
        pelaaja = self.stats.top(1, SortBy.GOALS)[0]
        self.assertAlmostEqual(pelaaja.name, "Lemieux")
    
    def test_eniten_avustuksia(self):
        pelaaja = self.stats.top(1, SortBy.ASSISTS)[0]
        self.assertAlmostEqual(pelaaja.name, "Gretzky")

    