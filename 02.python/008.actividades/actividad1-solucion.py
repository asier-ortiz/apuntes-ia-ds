"""
Crear una función que cuente el número de vocales en una cadena de texto
Consideraremos únicamente como vocales: a, e, i, o, u
"""


# Posible solución 1
def count_vowels1(text):
    return text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')


# Posible solución 2
def count_vowels2(text):
    num = 0
    for char in text:
        if char in 'aeiou':
            num += 1
    return num


print(count_vowels1("Hola buenas   prueba"))
print(count_vowels2("Hola buenas   prueba"))
print(count_vowels1(input('Introduce un texto para contar sus vocales: ')))
