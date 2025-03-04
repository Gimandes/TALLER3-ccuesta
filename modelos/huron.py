from modelos.animal_exotico import Animal_exotico

class Huron(Animal_exotico):
    def __init__(self, name:str, peso: float, edad: int, pais_de_origen: str, impuestos: float):
        super().__init__(name, peso, edad, pais_de_origen, impuestos)

    @staticmethod
    def hacer_sonido():
        return "¡Eek Eek!"
    
    def dar_informacion(self) -> str:
        return super().dar_informacion()

