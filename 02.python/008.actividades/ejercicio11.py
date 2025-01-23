"""
Imprimir el número de veces que la palabra python se repite en esta frase:
Python es un lenguaje de programación, PYTHON es multipropósito, python es un lenguaje interpretado
Sin utilizar el método count()
Nota: Pasar la frase a minúsculas
"""


def count_occurrences(phrase, word):
    count = 0
    for i in range(len(phrase) - 1):
        count += phrase[i:i + len(
            word)] == word  # Se suma resultado de una comparación (un boolean), True equivale a 1 y False a 0
    return count


word = 'python'
phrase = 'Python es un lenguaje de programación, PYTHON es multipropósito, python es un lenguaje interpretado'.lower()
print("Number of word \"python\" is in phrase: " + str(count_occurrences(phrase, word)) + " occurrences")
