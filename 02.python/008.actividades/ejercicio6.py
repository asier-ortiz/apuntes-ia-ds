"""
Verificar si un número introducido por el usuario es múltiplo de 5 y 7 o no
Probar con 33 y probar con 35
"""
number = int(input("Enter an integer: "))
if number % 5 == 0 and number % 7 == 0:
    print(number, "is a multiple of both 5 and 7")
else:
    print(number, "is not a multiple of both 5 and 7")
