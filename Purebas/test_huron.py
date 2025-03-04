import unittest
from modelos.huron import Huron

class TestHuron(unittest.TestCase):

    def setUp(self):
        self.huron = Huron(name="Huron Feliz", peso=5.0, edad=3, pais_de_origen="Argentina", impuestos=20.0)

    def test_hacer_sonido(self):
        self.assertEqual(self.huron.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete(self):
        self.assertEqual(self.huron.calcular_flete(), 5.0 * 10 + 20.0)
