import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(400)

    def test_luodussa_kassapaatessa_kaikki_oikein(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "0")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")

    def test_kateismaksu_riittava_rahamaara_ja_lounaat_kasvaa_edullinen(self):
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(400)), "160")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100240")
        self.assertEqual(str(self.kassapaate.edulliset), "1")

    def test_kateismaksu_riittava_rahamaara_ja_lounaat_kasvaa_maukas(self):
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(600)), "200")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100400")
        self.assertEqual(str(self.kassapaate.maukkaat), "1")

    def test_kateismaksu_ei_riittava_raha_ja_lounaat_ei_kasva_edullinen(self):
        self.assertEqual(str(self.kassapaate.syo_edullisesti_kateisella(200)), "200")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "0")

    def test_kateismaksu_ei_riittava_raha_ja_lounaat_ei_kasva_maukas(self):
        self.assertEqual(str(self.kassapaate.syo_maukkaasti_kateisella(200)), "200")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")

    def test_korttimaksu_riittava_rahamaara_ja_lounaat_kasvaa_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(str(self.maksukortti), "saldo: 1.6")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "1")

    def test_korttimaksu_riittava_rahamaara_ja_lounaat_kasvaa_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.maukkaat), "1")

    def test_korttimaksu_ei_riittava_kortinraha_ja_lounaat_ei_muutu_edullinen(self):
        self.maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.edulliset), "0")

    def test_korttimaksu_ei_riittava_kortinraha_ja_lounaat_ei_muutu_maukas(self):
        self.maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassapaate.maukkaat), "0")

    def test_ladataan_kortille_rahaa_saldo_ja_kassa_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100200")

    def test_ladataan_kortille_0_rahaa_saldo_ja_kassa_ei_kasva(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual(str(self.maksukortti), "saldo: 4.0")
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")