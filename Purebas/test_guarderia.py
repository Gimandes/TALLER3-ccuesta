import unittest
from modelos.guarderia import Guarderia

class TestGuarderia(unittest.TestCase):

    def setUp(self):
        self.guarderia = Guarderia()

    def test_alimentar_boa_exito(self):
        boa = self.guarderia.boas[0]
        mensaje = self.guarderia.alimentar_boa(boa)
        self.assertEqual(mensaje, "Éxito")

    def test_alimentar_boa_llena(self):
        boa = self.guarderia.boas[0]
        for _ in range(10):
            self.guarderia.alimentar_boa(boa)
        mensaje = self.guarderia.alimentar_boa(boa)
        self.assertEqual(mensaje, "La boa está llena")

    def test_alimentar_boa_inexistente(self):
        mensaje = self.guarderia.alimentar_boa(None)
        self.assertEqual(mensaje, "Esta Boa no existe!")