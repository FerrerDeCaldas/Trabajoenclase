#ejercicio 3

import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mostrar(self):
        print("Coordenada X:", self.x)
        print("Coordenada Y:", self.y)
    
    def mover(self, nueva_x, nueva_y):
        self.x = nueva_x
        self.y = nueva_y
    
    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)
        return distancia

punto1 = Punto(3, 4)
punto2 = Punto(-2, 7)


print("Coordenadas del Punto 1:")
punto1.mostrar()

print("Coordenadas del Punto 2:")
punto2.mostrar()

punto1.mover(6, 9)
print("Nuevas coordenadas del Punto 1:")
punto1.mostrar()


distancia = punto1.calcular_distancia(punto2)
print("Distancia entre el Punto 1 y el Punto 2:", distancia)