import datetime

products = []
product_properties = ['name', 'price', 'stock']


# Función que lee los datos de un producto desde input
def get_product():
    product_dict = dict()
    read = True
    while read:
        try:
            product_dict["name"] = product_dict["name"] if "name" in product_dict else str(
                input("Introduzca nombre del producto {}: ".format(i + 1)))
            product_dict["price"] = product_dict["price"] if "price" in product_dict else float(
                input("Introduzca precio del producto {}: ".format(i + 1)))
            product_dict["stock"] = product_dict["stock"] if "stock" in product_dict else int(
                input("Introduzca stock del producto {}: ".format(i + 1)))
            read = False
        except ValueError:
            print("Error al leer la información de producto, vuelva a introducir el dato de nuevo.")

    product_dict["creation_date"] = datetime.datetime.now().year
    product_dict["update_date"] = datetime.datetime.now()
    return product_dict


# 1. Leemos los datos de los productos
print("Introduzca a continuación datos de productos")
for i in range(3):
    products.append(get_product())

# 2. Leemos la acción a realizar
action = ''
while action != 'salir':
    try:
        action = str(input("Introduzca la accion que desea realizar \"editar\" o \"salir\": "))
        if action != "editar":
            continue

        # 3. Leemos el índice del producto a modificar
        product_index = int(
            input("Introduzca el índice del producto que desea editar de 1 a {}: ".format(len(products))))
        property_edit = ''
        while property_edit not in product_properties:
            # 4. Leemos el nombre de la propiedad que se desea editar
            property_edit = str(input("Introduzca la propiedad que desea editar: \"name\", \"price\", \"stock\": "))
            if property_edit not in product_properties:
                continue

            # 5. Leemos el nuevo valor para la propiedad que se desea editar
            if property_edit == "name":
                products[product_index - 1]["name"] = str(
                    input("Introduzca el nuevo nombre del producto {}: ".format(product_index)))
            elif property_edit == "price":
                products[product_index - 1]["price"] = float(
                    input("Introduzca el nuevo precio del producto {}: ".format(product_index)))
            elif property_edit == "stock":
                products[product_index - 1]["stock"] = int(
                    input("Introduzca el nuevo stock del producto {}: ".format(product_index)))

            # 6. Nos aseguramos de actualizar la fecha de actualización
            products[product_index - 1]["update_date"] = datetime.datetime.now()
            print("Producto {} modificado correctamente.".format(products[product_index - 1]["name"]))
    except ValueError:
        print("Se ha producido un error al intentar realizar una acción sobre los productos.")
    except IndexError:
        print("El índice de producto introducido no es válido, introduzca un nuevo índice")

print("La base de productos es la siguiente:")
print(products)
