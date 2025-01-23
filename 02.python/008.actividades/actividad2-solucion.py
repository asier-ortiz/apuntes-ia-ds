"""
Crear una función que dada una cadena de texto como parámetro devuelva una nueva cadena de texto
que duplique cada caracter por el número de posición en el que se encuentre, separándolos por guiones,
y la primera letra de cada caracter en mayúscula, ejemplo:

acumulador("abcd") devuelve "A-Bb-Ccc-Dddd"
acumulador("RqaEzty") devuelve "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
acumulador("cwAt") devuelve "C-Ww-Aaa-Tttt"

"""


def acumulador(text):
    text = text.lower()
    result = ""
    for i in range(len(text)):
        result += text[i].upper()  # Primero establecemos la primera letra en mayúsculas
        result += text[i] * i  # Después repetimos la letra tantas veces según su posición
        if i < len(text) - 1:
            result += "-"  # Añadimos un guión a todas menos a la última sucesión de letras
    return result


print(acumulador("abcd"))
print(acumulador("RqaEzty"))
print(acumulador("cwAt"))
