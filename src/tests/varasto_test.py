import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_liika_ottaminen_ei_onnistu(self):
        self.varasto.lisaa_varastoon(5)
        result = self.varasto.ota_varastosta(6)
        self.assertNotEqual(result, 6)

    def test_liika_tavaraa_lisaaminen_ei_onnistu(self):
        self.varasto.lisaa_varastoon(20)
        self.assertEqual(self.varasto.saldo, 10)

    def test_negatiivinen_tilavuus_ei_sallita(self):
        uusi_varasto = Varasto(-10)
        self.assertEqual(uusi_varasto.tilavuus, 0)

    def test_alkusaldo_ei_saa_olla_negatiivinen(self):
        uusi_varasto = Varasto(10, -10)
        self.assertAlmostEqual(uusi_varasto.saldo, 0)

    def test_lisaaminen_negatiivisella_ei_onnisut(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_ottaminen_negatiivisella_ei_onnistu(self):
        result = self.varasto.ota_varastosta(-10)
        self.assertAlmostEqual(result, 0)

    def test_varasto_oliolla_on_str_metodi_toimii(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")