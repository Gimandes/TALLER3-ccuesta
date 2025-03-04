from modelos.boa import Boa
from modelos.huron import Huron

class Guarderia:

    def __init__(self):
        self.boas = [
            Boa(name="Boa1", peso=15.0, edad=5, pais_de_origen="Brasil", impuestos=30.0),
            Boa(name="Boa2", peso=18.0, edad=6, pais_de_origen="Colombia", impuestos=35.0)
        ]
        self.hurones = [
            Huron(name="Huron1", peso=4.5, edad=3, pais_de_origen="Argentina", impuestos=20.0),
            Huron(name="Huron2", peso=5.0, edad=4, pais_de_origen="Chile", impuestos=25.0)
        ]

    def alimentar_boa(self, boa: Boa) -> str:
        if boa is None:
            return "Esta Boa no existe!"

        try:
            boa.alimentar()
            return "Éxito"
        except ValueError as e:
            if str(e) == "Demasiados Ratones!":
                return "La boa está llena"
            else:
                raise