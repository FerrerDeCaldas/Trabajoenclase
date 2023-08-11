
#Ejercicio 1

class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje


vehiculo1 = Vehiculo(200, 15000)
vehiculo2 = Vehiculo(180, 22000)


print("Vehículo 1 - Velocidad Máxima:", vehiculo1.velocidad_maxima)
print("Vehículo 1 - Kilometraje:", vehiculo1.kilometraje)

print("Vehículo 2 - Velocidad Máxima:", vehiculo2.velocidad_maxima)
print("Vehículo 2 - Kilometraje:", vehiculo2.kilometraje)



