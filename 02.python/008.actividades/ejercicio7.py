"""
Encontrar la media de 10 números utilizando un bucle indeterminado
"""
count = 0
total_sum = 0.0
print("Introduzca 10 números")
while count < 10:
    number = float(input("Introduzca el {} número: ".format(count + 1)))
    count += 1
    total_sum += number
avg = total_sum / 10
print("La media de los 10 números introducidos es:", avg)
