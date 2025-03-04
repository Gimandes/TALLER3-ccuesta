from abc import ABC, abstractmethod
from modelos.ianimal import iAnimal 

class Animal(iAnimal, ABC): 
    def __init__(self, name: str, peso: float, edad: int):
        self._name= name
        self._peso = peso 
        self._edad = edad
        self._kilogramos_comidos=0

    @abstractmethod
    def hacer_sonido(self)-> str:
        pass

    @abstractmethod
    def comer(self, kilos):
        self._kilogramos_comidos += kilos

    @abstractmethod
    def obtener_kilos_comidos(self)-> float:
        return self._kilogramos_comidos

    @property
    def name(self):
        return self._name
    
    @property
    def peso(self):
        return self._peso
    
    @property
    def edad(self):
        return self._edad    

