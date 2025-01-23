"""
Calcular la media de un conjunto de números que el usuario introduce por entrada
"""

count = int(input("Enter the count of numbers: "))
i = 0
total_sum = 0
for i in range(count):
    x = int(input("Enter an integer: "))
    total_sum = total_sum + x
avg = total_sum / count

print(" The average is: ", avg)
