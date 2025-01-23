"""
Ejercicio 3:
Crear un programa python que lea 5 productos con 5 precios y muestre una tabla con dichos datos
Crear 3 2.funciones
    - Una función que permita conocer si un precio es Caro o Barato en base a si es mayor o igual que 20 €
    - Una función que elimine los espacios de un producto y lo convierta a minúsculas
    - Una función que reemplace las palabras: tomate, tortilla por asteriscos

Ejemplo de resultado:
Introduce nombre de producto 1: TORTillA
Introduce precio de producto 1: 21.22 
Introduce nombre de producto 2: Puerro
Introduce precio de producto 2: 3.99
Introduce nombre de producto 3: TOMATE
Introduce precio de producto 3: 5.99
Introduce nombre de producto 4: Espinacas
Introduce precio de producto 4: 21.23
Introduce nombre de producto 5: Queso fresco
Introduce precio de producto 5: 29.99
************************* LISTA DE LA COMPRA *************************
Producto        Precio          Valor
********           21.22             Caro             
puerro             3.99              Barato           
******             5.99              Barato           
espinacas          21.23             Caro             
queso fresco       29.99             Caro  
"""


VALUE_PRICE = 20
def valueCalculator(price):
    return str(price >= VALUE_PRICE).replace("True", "Caro").replace("False", "Barato")

def nameAdaptor(name):
    return name.strip().lower()

def nameMasker(name):
    name = name.replace("tortilla", "*" * len("tortilla"))
    name = name.replace("tomate", "*" * len("tomate"))
    return name

prod1 = nameMasker(nameAdaptor(str(input("Introduce nombre de producto 1: "))))
price1 = float(input("Introduce precio de producto 1: "))
value1 = valueCalculator(price1)

prod2 = nameMasker(nameAdaptor(str(input("Introduce nombre de producto 2: "))))
price2 = float(input("Introduce precio de producto 2: "))
value2 = valueCalculator(price2)

prod3 = nameMasker(nameAdaptor(str(input("Introduce nombre de producto 3: "))))
price3 = float(input("Introduce precio de producto 3: "))
value3 = valueCalculator(price3)

prod4 = nameMasker(nameAdaptor(str(input("Introduce nombre de producto 4: "))))
price4 = float(input("Introduce precio de producto 4: "))
value4 = valueCalculator(price4)

prod5 = nameMasker(nameAdaptor(str(input("Introduce nombre de producto 5: "))))
price5 = float(input("Introduce precio de producto 5: "))
value5 = valueCalculator(price5)
        
print("*" * 25 + " LISTA DE LA COMPRA " + "*" * 25)
print("Producto\tPrecio\t\tValor")
print("{0:<18} {1:<17} {2:<17}".format(prod1, price1, value1))
print("{0:<18} {1:<17} {2:<17}".format(prod2, price2, value2))
print("{0:<18} {1:<17} {2:<17}".format(prod3, price3, value3))
print("{0:<18} {1:<17} {2:<17}".format(prod4, price4, value4))
print("{0:<18} {1:<17} {2:<17}".format(prod5, price5, value5))
