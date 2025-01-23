"""
Dado un número leído de la entrada imprimir si es par o impar
"""

number = input("Enter a number ")
x = int(number) % 2
if x == 0:
    print(" The number is even ")
else:
    print(" The number is odd ")
