"""
Verificar si un número introducido por el usuario es múltiplo de 5 o no
"""
number = int(input("Enter an integer: "))
if number % 5 == 0:
    print(number, "is a multiple of 5")
else:
    print(number, "is not a multiple of 5")
