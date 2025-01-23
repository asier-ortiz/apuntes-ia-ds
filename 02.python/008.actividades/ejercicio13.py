"""
Crear una función que reciba 3 parámetros:
- un diccionario que representa la mercancía en stock en una tienda
- una cadena de texto que representa un producto que un cliente quiere comprar
- un número entero que representa las unidades de producto que el cliente quiere comprar
La función debe devolver True si el diccionario contiene el producto en stock suficiente, False en caso contrario
"""


def check_stock(stock_data, merch, qty):
    return stock_data.get(merch, 0) >= qty


stock = {
    "prod1": 2,
    "prod2": 4
}
result = check_stock(stock, "prod2", 1)
print(result)

result = check_stock(stock, "prod2", 5)
print(result)

result = check_stock(stock, "prod3", 1)
print(result)
