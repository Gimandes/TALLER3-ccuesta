from modelos.animal_exotico import Animal_exotico


class Boa(Animal_exotico):
    def __init__(self, name: str, peso: float, edad: int, pais_de_origen: str, impuestos: float) -> None:
        super().__init__(name, peso, edad, pais_de_origen, impuestos)
        self._num_ratones = 0

    @staticmethod
    def hacer_sonido() -> str:
        return "¡Tssss!"
    
    def alimentar(self):
        if self._num_ratones >= 20:
            raise ValueError("Demasiados Ratones!")
        self._num_ratones += 1
        self.peso += 0.5


    @property
    def ratones_comidos(self) -> int:
        return self._num_ratones
    

    
    def dar_informacion(self):
        return f"{super().dar_informacion()} - Ratones comidos: {self.ratones_comidos}"
