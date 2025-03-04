from modelos.boa import Boa 
from modelos.huron import Huron 


boa1 = Boa("Boa1", 8.3,5,"Colombia", 0.3)
huron1 = Huron("huron1", 4.2, 1, "Colombia", 0.2)


# Imprimir información
print(f"{huron1.dar_informacion()} - Sonido: {huron1.hacer_sonido()}")
print(f"{boa1.dar_informacion()} - Sonido: {boa1.hacer_sonido()}")

# Alimentar a la boa
for x in range(25):
    boa1.comer_raton()

print(f"La boa ha comido {boa1.ratones_comidos} ratón(es).")

#calcular_flete
print(f"Flete de la Boa: {boa1.calcular_flete()} \nFlete del Huhron:  {huron1.calcular_flete()}")