'''
Leer 10 números enteros positivos mayores que 0 de la consola y calcular la media
'''
count = 0
sum = 0
while count<10:
    number = int(input("Introduce el {} número entero positivo: ".format(count + 1)))
    if number <= 0:
        continue
    count += 1
    sum += number
print("La media de los 10 números introducidos es: {}".format(sum/10))