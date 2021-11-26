import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteen_hinta(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_2_tavaraa(self):
        maito = Tuote("maito", 3)
        piima = Tuote("piimä", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(piima)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahdent_eri_tuotteen_lisaamisen_jalkeen_hinta_on_niiden_summa(self):
        maito = Tuote("maito", 3)
        piima = Tuote("piimä", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(piima)
        self.assertEqual(self.kori.hinta(), 7)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_2_tavaraa(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
