"""
Ejemplo sin sobrecarga de operadores
"""
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)


punto_a = Punto(5, 5)
punto_b = Punto(2, 2)
punto_suma = punto_a + punto_b
print("punto_suma: x=", punto_suma.x, ", y=", punto_suma.y)
