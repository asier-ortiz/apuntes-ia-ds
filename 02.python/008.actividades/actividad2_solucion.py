
"""
Ejercicio 2:
Crear un programa que lea 5 nombres de producto y sus precios y los muestre en formato tabla
La tabla tendrá 3 columnas, una con el nombre de producto, otra con el precio y la otra con un texto 
Barato o Caro en función de si el precio es mayor de 5 €, hacer esto sin utilizar estructuras if
Pista: usar el método predefinido replace
Ejemplo de resultado:

Introduce nombre de producto 1: Tomate
Introduce precio de producto 1: 4.99
Introduce nombre de producto 2: Queso
Introduce precio de producto 2: 5.01
Introduce nombre de producto 3: Espinacas
Introduce precio de producto 3: 2.99
Introduce nombre de producto 4: Tortilla
Introduce precio de producto 4: 3.99
Introduce nombre de producto 5: Aguacate
Introduce precio de producto 5: 8.99
************************* LISTA DE LA COMPRA *************************
Producto        Precio              Valor
Tomate             4.99              Barato
Queso              5.01              Caro
Espinacas          2.99              Barato
Tortilla           3.99              Barato
Aguacate           8.99              Caro
"""
prod1 = str(input("Introduce nombre de producto 1: "))
price1 = float(input("Introduce precio de producto 1: "))
value1 = str(price1 > 5).replace("True", "Caro").replace("False", "Barato")

prod2 = str(input("Introduce nombre de producto 2: "))
price2 = float(input("Introduce precio de producto 2: "))
value2 = str(price2 > 5).replace("True", "Caro").replace("False", "Barato")

prod3 = str(input("Introduce nombre de producto 3: "))
price3 = float(input("Introduce precio de producto 3: "))
value3 = str(price3 > 5).replace("True", "Caro").replace("False", "Barato")

prod4 = str(input("Introduce nombre de producto 4: "))
price4 = float(input("Introduce precio de producto 4: "))
value4 = str(price4 > 5).replace("True", "Caro").replace("False", "Barato")

prod5 = str(input("Introduce nombre de producto 5: "))
price5 = float(input("Introduce precio de producto 5: "))
value5 = str(price5 > 5).replace("True", "Caro").replace("False", "Barato")


print("*" * 25 + " LISTA DE LA COMPRA " + "*" * 25)
print("Producto\tPrecio\tValor" )
print("{0:<18} {1:<17} {2}".format(prod1, price1, value1))
print("{0:<18} {1:<17} {2}".format(prod2, price2, value2))
print("{0:<18} {1:<17} {2}".format(prod3, price3, value3))
print("{0:<18} {1:<17} {2}".format(prod4, price4, value4))
print("{0:<18} {1:<17} {2}".format(prod5, price5, value5))