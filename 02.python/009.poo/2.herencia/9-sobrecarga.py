"""
Ejemplo sin sobrecarga de operadores
"""
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


punto_a = Punto(5, 5)
punto_b = Punto(2, 2)

suma_x = punto_a.x + punto_b.x
suma_y = punto_a.y + punto_b.y

punto_suma = Punto(suma_x, suma_y)

print(punto_suma.x)
print(punto_suma.y)
