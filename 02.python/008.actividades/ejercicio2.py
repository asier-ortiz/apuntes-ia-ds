"""
Teniendo en cuenta que la fórmula para convertir grados celsius a grados Fahrenheit es:

F = 9*C/5 + 32

Leer un número por consola que represente la temperatura en grados centígrados y
la imprima en grados fahrenheit.
"""

celsius = int(input(" Enter temperature in Centigrade: "))
fahrenheit = 9 * celsius / 5 + 32

print(" Temperature in Fahrenheit is: ", fahrenheit)
