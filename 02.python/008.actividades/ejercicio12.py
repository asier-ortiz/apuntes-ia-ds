"""
Dadas dos listas de números:
Primera lista: [12, 34, 56, 99, 76, 11, 156, 66, 59, 31]
Segunda lista: [98, 43, 55, 68, 42, 56, 21, 13, 15, 17, 99, 96]
Crear una nueva lista que contenga los números pares de la primera y después los números impares de la segunda
Imprimir la nueva lista por consola
"""

first_list = [12, 34, 56, 99, 76, 11, 156, 66, 59, 31]
second_list = [98, 43, 55, 68, 42, 56, 21, 13, 15, 17, 99, 96]
result_list = []

for num in first_list:
    if num % 2 == 0:
        result_list.append(num)

for num in second_list:
    if num % 2 != 0:
        result_list.append(num)

print(result_list)
# Resultado esperado:
# [12, 34, 56, 76, 156, 66, 43, 55, 21, 13, 15, 17, 99]
