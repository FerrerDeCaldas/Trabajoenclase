#ejercicio 4

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangulo:
    def __init__(self, esquina1, esquina2):
        self.esquina1 = esquina1
        self.esquina2 = esquina2
    
    def calcular_lados(self):
        lado_x = abs(self.esquina1.x - self.esquina2.x)
        lado_y = abs(self.esquina1.y - self.esquina2.y)
        return lado_x, lado_y
    
    def calcular_perimetro(self):
        lado_x, lado_y = self.calcular_lados()
        return 2 * (lado_x + lado_y)
    
    def calcular_area(self):
        lado_x, lado_y = self.calcular_lados()
        return lado_x * lado_y
    
    def es_cuadrado(self):
        lado_x, lado_y = self.calcular_lados()
        return lado_x == lado_y

esquina1 = Punto(1, 1)
esquina2 = Punto(4, 3)
rectangulo = Rectangulo(esquina1, esquina2)

print("Perímetro:", rectangulo.calcular_perimetro())
print("Área:", rectangulo.calcular_area())
print("¿Es un cuadrado?:", rectangulo.es_cuadrado())
