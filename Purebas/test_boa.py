import unittest
from modelos.boa import Boa

class TestBoa(unittest.TestCase):

    def setUp(self):
        self.boa = Boa(name="Boa Constrictor", peso=15.0, edad=5, pais_de_origen="Brasil", impuestos=30.0)

    def test_hacer_sonido(self):
        self.assertEqual(self.boa.hacer_sonido(), "¡Tssss!")

    def test_calcular_flete(self):
        self.assertEqual(self.boa.calcular_flete(), 15.0 * 10 + 30.0)

    def test_alimentar(self):
        for _ in range(10):
            self.boa.alimentar()
        with self.assertRaises(ValueError) as context:
            self.boa.alimentar()
        self.assertEqual(str(context.exception), "Demasiados Ratones!")

