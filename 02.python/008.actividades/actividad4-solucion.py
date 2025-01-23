"""
Crear una función que reciba como parámetro un número entero positivo y calcule su persistencia multiplicativa, que consiste
en el número de veces que hay que multiplicar sus dígitos hasta obtener como resultado un número de un sólo dígito.

Ejemplo

Si introducimos 39 obtenemos 3 porque:
3*9 = 27, 2*7 = 14, 1*4=4
4 tiene solo un dígito

Si introducimos 999 obtenemos 4 porque:
9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12,  1*2 = 2
2 tiene solo un dígito

Si introducimos 4 obtenemos 0 porque:
4 tiene solo un dígito

"""


def persistence(num):
    num = str(num)
    count = 0
    while len(num) > 1:
        multiplication = 1
        for i in num:
            multiplication *= int(i)
        num = str(multiplication)
        count += 1
    return count


print(persistence(39))
print(persistence(999))
print(persistence(4))
