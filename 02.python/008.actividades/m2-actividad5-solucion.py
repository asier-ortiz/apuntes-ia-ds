import datetime

products = []
product_properties = ['name', 'price', 'stock']

print("Introduzca a continuación datos de productos:")
for i in range(3):
    product_dict = dict()
    product_dict["name"] = str(input("Introduzca nombre del producto {}: ".format(i + 1)))
    product_dict["price"] = float(input("Introduzca precio del producto {}: ".format(i + 1)))
    product_dict["stock"] = int(input("Introduzca stock del producto {}: ".format(i + 1)))
    product_dict["creation_date"] = datetime.datetime.now().year
    product_dict["update_date"] = datetime.datetime.now()
    products.append(product_dict)

action = ''
while action != 'salir':
    action = str(input("Introduzca la accion que desea realizar \"editar\" o \"salir\": "))
    if action != "editar":
        continue

    product_index = int(input("Introduzca el índice del producto que desea editar de 1 a {}: ".format(len(products))))
    property_edit = ''
    while property_edit not in product_properties:
        property_edit = str(input("Introduzca la propiedad que desea editar: \"name\", \"price\", \"stock\": "))
        if property_edit not in product_properties:
            continue

        if property_edit == "name":
            products[product_index - 1]["name"] = str(
                input("Introduzca el nuevo nombre del producto {}: ".format(product_index)))
        elif property_edit == "price":
            products[product_index - 1]["price"] = float(
                input("Introduzca el nuevo precio del producto {}: ".format(product_index)))
        elif property_edit == "stock":
            products[product_index - 1]["stock"] = int(
                input("Introduzca el nuevo stock del producto {}: ".format(product_index)))

        products[product_index - 1]["update_date"] = datetime.datetime.now()
        print("Producto {} modificado correctamente.".format(products[product_index - 1]["name"]))

print("La base de productos es la siguiente:")
print(products)
