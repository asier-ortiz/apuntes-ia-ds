"""

Leer una cadena de texto por consola.

Crear una función que imprima por consola aquellas letras de la cadena de texto con índices impares utilizando un bucle for

"""


def print_even_index_chars(text):
    for i in range(0, len(text) - 1, 2):
        print("word[{}] = {}".format(i + 1, text[i]))


word = str(input("Introduce una palabra: "))
print_even_index_chars(word)
