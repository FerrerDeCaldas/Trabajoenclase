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