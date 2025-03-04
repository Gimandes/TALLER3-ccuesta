from modelos.animal import Animal

class Animal_exotico(Animal):
    def __init__(self, name:str, peso: float, edad: int, pais_de_origen: str, impuestos: float) -> None: 
        super().__init__(name, peso, edad)  # Hereda nombre, peso y edad de 'Animal'
        self._pais_de_origen = pais_de_origen
        self._impuestos = impuestos 
        self._kilos_comidos = 0

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, nuevo_peso):
        self._peso = nuevo_peso

    @property
    def pais_de_origen(self) -> str:
        """ Devuelve el valor del atributo privado 'pais_de_origen' """
        return self._pais_de_origen
    
    @pais_de_origen.setter
    def pais_de_origen(self, value: str) -> None:
        """ Establece un nuevo valor para el atributo privado 'pais_de_origen' """
        if isinstance(value, str):
            self._pais_de_origen = value
        else:
            raise ValueError('Expected str')
        
    @property
    def impuestos(self) -> float:
        """ Devuelve el valor del atributo privado 'impuestos' """
        return self._impuestos
    
    @impuestos.setter
    def impuestos(self, value: float) -> None:
        """ Establece un nuevo valor para el atributo privado 'impuestos' """
        if isinstance(value, float):
            self._impuestos = value
        else:
            raise ValueError('Expected float')
        
    def calcular_flete(self) -> float:
        return self.peso * 10 + self.impuestos
    
    def comer(self, kilos: float) -> float:
        if kilos > 0:
            self._kilos_comidos += kilos
        else:
            raise ValueError("La cantidad de comida debe ser mayor a 0")

    def obtener_kilos_comidos(self) -> float:
        return self._kilos_comidos
    
    def dar_informacion(self) -> str:
        return f"Nanme: {self.name}, Peso: {self.peso} kg, Edad: {self.edad} años, Origen: {self.pais_de_origen}, Impuestos: {self.impuestos}"

