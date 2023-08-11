#ejercicio 6

class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

class Pintas:
    CORAZON = "Corazón"
    DIAMANTE = "Diamante"
    TREBOL = "Trébol"
    ESPADA = "Espada"


carta1 = Carta("As", Pintas.CORAZON)
carta2 = Carta("10", Pintas.TREBOL)


print("Carta 1 - Valor:", carta1.valor, "Pinta:", carta1.pinta)
print("Carta 2 - Valor:", carta2.valor, "Pinta:", carta2.pinta)