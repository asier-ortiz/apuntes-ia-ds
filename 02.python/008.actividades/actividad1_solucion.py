
"""
Ejercicio 1 - Imprimir por consola una tabla que muestre una lista de la compra con 5 filas y 4 columnas:
1 columna muestra el nombre del producto
2 columna muestra la cantidad de producto
3 columna muestra el precio por unidad
4 columna muestra el precio total en base a las unidades
Definir los datos en variables primero, utilizaremos datos inventados

Ejemplo:
    ************************* LISTA DE LA COMPRA *************************
    Producto        Cantidad        Precio Unidad   Precio Total
    Leche              5                 2.66           13.30
    Huevos             1                 1.45           1.45
    Harina             4                 0.99           3.96
    Tomate frito       2                 1.11           2.22
    Queso              3                 5.67           17.01
    **********************************************************************
    TOTAL                                               37.94
    **********************************************************************
"""

prod1,  prod2,  prod3,  prod4,  prod5 = "Leche", "Huevos", "Harina", "Tomate frito", "Queso" 
qty1, qty2, qty3, qty4, qty5 = 5, 1, 4, 2, 3
priceUnit1, priceUnit2, priceUnit3, priceUnit4, priceUnit5 = 2.66, 1.45, 0.99, 1.11, 5.67
totalPrice = qty1*priceUnit1 + qty2*priceUnit2 + qty3*priceUnit3 + qty4*priceUnit4 + qty5*priceUnit5

print("*" * 25 + " LISTA DE LA COMPRA " + "*" * 25)
print("Producto\tCantidad\tPrecio Unidad\tPrecio Total" )
print("{0:<18} {1:<17} {2:<14} {3:.2f}".format(prod1, qty1, priceUnit1, qty1*priceUnit1))
print("{0:<18} {1:<17} {2:<14} {3:.2f}".format(prod2, qty2, priceUnit2, qty2*priceUnit2))
print("{0:<18} {1:<17} {2:<14} {3:.2f}".format(prod3, qty3, priceUnit3, qty3*priceUnit3))
print("{0:<18} {1:<17} {2:<14} {3:.2f}".format(prod4, qty4, priceUnit4, qty4*priceUnit4))
print("{0:<18} {1:<17} {2:<14} {3:.2f}".format(prod5, qty5, priceUnit5, qty5*priceUnit5))
print("*" * 70)
print("{0:<18} {1:<17} {2:<14} {3:.2f}".format("TOTAL", "", "", totalPrice))
print("*" * 70)