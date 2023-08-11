
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



#Ejercicio 2
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

punto1 = Punto(3, 4)
punto2 = Punto(-2, 7)

print("Punto 1 - Coordenada X:", punto1.x)
print("Punto 1 - Coordenada Y:", punto1.y)

print("Punto 2 - Coordenada X:", punto2.x)
print("Punto 2 - Coordenada Y:", punto2.y)



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



#ejercicio 7,8,9,10,11

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
    
    def depositar(self, cantidad):
        self.balance += cantidad
    
    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
        else:
            print("Saldo insuficiente para realizar el retiro.")
    
    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
    
    def mostrar_detalles(self):
        print("Número de Cuenta:", self.numero_cuenta)
        print("Propietarios:", ", ".join(self.propietarios))
        print("Balance:", self.balance)


cuenta = CuentaBancaria("12345", ["Juan", "María"], 1000)


print("Detalles iniciales:")
cuenta.mostrar_detalles()


cuenta.depositar(500)
cuenta.retirar(200)
cuenta.aplicar_cuota_manejo()


print("\nDetalles después de las operaciones:")
cuenta.mostrar_detalles()