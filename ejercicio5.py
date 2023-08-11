#ejercicio 5

import math

class Punto:
    def __init__(self, x, y): self.x, self.y = x, y

class Circulo:
    def __init__(self, centro, radio): self.centro, self.radio = centro, radio
    def area(self): return math.pi * self.radio ** 2
    def perimetro(self): return 2 * math.pi * self.radio
    def punto_pertenece(self, punto): return (punto.x - self.centro.x)**2 + (punto.y - self.centro.y)**2 <= self.radio ** 2

centro = Punto(0, 0)
circulo = Circulo(centro, 5)

print("Área:", circulo.area())
print("Perímetro:", circulo.perimetro())

punto1 = Punto(3, 3)
punto2 = Punto(7, 7)

print("¿Punto 1 pertenece al círculo?:", circulo.punto_pertenece(punto1))
print("¿Punto 2 pertenece al círculo?:", circulo.punto_pertenece(punto2))