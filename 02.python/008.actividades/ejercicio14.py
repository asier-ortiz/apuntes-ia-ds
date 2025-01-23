"""
Crea una función que reciba una cadena de texto como parámetro y devuelva:
True en caso de que haya el mismo número de 'x' y de 'o'
False en caso contrario
El método debe ser insensitivo a mayúsculas
"""


def check_xo(sentence):
    sentence = sentence.lower()
    return sentence.count("x") == sentence.count("o")


print(check_xo('xo'))
print(check_xo('xo0'))
print(check_xo('xxxoo'))
