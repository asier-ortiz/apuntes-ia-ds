"""
Dada una lista de 5 números enteros leídos por la consola, imprimir True si el primer elemento y el último son iguales
"""
NUMBERS = 5


def read_numbers():
    number_list = []
    for i in range(NUMBERS):
        number_list.append(int(input("Enter an integer number: ")))
    return number_list


def check_first_last(number_list):
    if len(number_list) < 2:  # Comprobamos que haya al menos 2 elementos antes de hacer nada
        return False
    if number_list[0] == number_list[-1]:
        return True
    else:
        return False


numbers = read_numbers()
result = check_first_last(numbers)
print("First and last elements are equals: " + str(result))
