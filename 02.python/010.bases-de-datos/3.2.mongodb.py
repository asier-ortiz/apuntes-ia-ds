"""
MongoDB CRUD
"""

import pymongo
from bson.objectid import ObjectId

mongoParameters = 'mongodb://root:password@localhost:27017/'


class Product:
    # Clase para representar los productos de la tabla products en base de datos

    def __init__(self, id, name, sku, quantity, price):
        self.id = id
        self.name = name
        self.sku = sku
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f'Product(id:{self.id}, name:{self.name}, sku:{self.sku}, quantity:{self.quantity}, price:{self.price})'

    def __repr__(self):
        return self.__str__()


# ********************* FUNCIONES PARA LECTURA DE PRODUCTOS POR CONSOLA ******************************************

def read_new_product_input():
    """
    Lee los datos de un nuevo producto introducido por el usuario a través de la consola.
    El producto no tiene id ya que todavía no existe en base de datos.
    Returns
    -------
    product
        un objeto de la clase Product con los datos leídos de la consola
    """
    name, sku, quantity, price = '', '', 0, 0.0
    read = True
    while read:
        try:
            name = name if name else str(input("Introduce el nombre de producto: "))
            sku = sku if sku else str(input("Introduce el sku de producto: "))
            quantity = quantity if quantity else int(input("Introduce la cantidad de producto: "))
            price = price if price else float(input("Introduce el precio del producto: "))
            read = False
        except ValueError as e:
            print(e)
    return Product(None, name, sku, quantity, price)


def read_product_input():
    """
    Lee los datos de un producto existente introducidos por el usuario a través de la consola.
    Necesario que el producto tenga un id.
    Returns
    -------
    product
        un objeto de la clase Product con los datos leídos de la consola
    """
    product_id, name, sku, quantity, price = '', '', '', 0, 0.0
    read = True
    while read:
        try:
            product_id = product_id if product_id else str(input("Introduce el id de producto a modificar: "))
            name = name if name else str(input("Introduce el nuevo nombre de producto: "))
            sku = sku if sku else str(input("Introduce el nuevo sku de producto: "))
            quantity = quantity if quantity else int(input("Introduce la nueva cantidad de producto: "))
            price = price if price else float(input("Introduce el nuevo precio del producto: "))
            read = False
        except ValueError as e:
            print(e)
    return Product(product_id, name, sku, quantity, price)


# ********************* FUNCIONES CRUD ***************************************************************

def create_product(product):
    """
    Crea un producto en base de datos

    Parámetros
        ----------
        product : Product
            Objeto producto con los datos de producto para almacenar en base de datos
    """
    try:
        client = pymongo.MongoClient(mongoParameters)
        database = client["ecommerce"]
        collection = database["products"]

        new_product = {
            "name": product.name,
            "sku": product.sku,
            "quantity": product.quantity,
            "price": product.price
        }
        result = collection.insert_one(new_product)
        print("Nuevo producto insertado con ID: ", result.inserted_id)

    except Exception as e:
        print("Error inserting one product from database", e)
    finally:
        client.close()


def update_product(product):
    """
    Actualiza un producto existente en base de datos

    Parámetros
        ----------
        product : Product
            Objeto producto con los datos de producto para almacenar en base de datos
    """
    try:
        client = pymongo.MongoClient(mongoParameters)
        database = client["ecommerce"]
        collection = database["products"]

        # Para actualizar un documento utilizamos update_one
        query = {"_id": ObjectId(product.id)}
        updated_product = {"$set": {
            "name": product.name,
            "sku": product.sku,
            "quantity": product.quantity,
            "price": product.price
        }
        }

        result = collection.update_one(query, updated_product)
        print(result.modified_count, "documento/s modificado/s")

    except Exception as e:
        print("Error updating product from database", e)
    finally:
        client.close()


def find_product_by_id(id):
    """
    Recupera un producto de base de datos a partir de su id

    Parámetros
        ----------
        id : int
            El identificador del producto a recuperar de base de datos
    Returns
    -------
    list
        una lista de productos
    """
    try:
        client = pymongo.MongoClient(mongoParameters)
        database = client["ecommerce"]
        collection = database["products"]

        query = {"_id": ObjectId(id)}
        product_db = collection.find_one(query)
        if product_db:
            return Product(product_db["_id"], product_db["name"], product_db["sku"], product_db["quantity"],
                           product_db["price"])

    except Exception as e:
        print("Error retrieving product from database", e)
    finally:
        client.close()


def find_all_products():
    """
    Recupera todos los productos de base de datos

    Returns
    -------
    list
        una lista de productos
    """
    try:
        client = pymongo.MongoClient(mongoParameters)
        database = client["ecommerce"]
        collection = database["products"]

        product_dict = collection.find()
        if product_dict:
            product_list = []
            for element in product_dict:
                product_list.append(
                    Product(element["_id"], element["name"], element["sku"], element["quantity"], element["price"]))
            return product_list

    except Exception as e:
        print("Error retrieving products from database", e)
    finally:
        client.close()


def delete_product(id):
    """
    Borra un producto de la base de datos a partir de su campo id

    Parámetros
        ----------
        id : int
            El identificador del producto a eliminar de base de datos
    """
    try:
        client = pymongo.MongoClient(mongoParameters)
        database = client["ecommerce"]
        collection = database["products"]

        query = {"_id": ObjectId(id)}
        result = collection.delete_one(query)
        print(result.deleted_count, "documento/s eliminado/s")
    except Exception as e:
        print("Error deleting product from database", e)
    finally:
        client.close()


# ********************* CÓDIGO PARA EL PROGRAMA ***************************************************************

action = 0
while action != 6:
    try:
        action = int(input(
            "\nIntroduce una acción a realizar:\n"
            "1 - Consultar producto \n"
            "2 - Consultar todos los productos\n"
            "3 - Crear producto \n"
            "4 - Modificar producto\n"
            "5 - Borrar producto \n"
            "6 - Salir\n"))

        if action == 1:  # Consultar producto
            prodId = str(input("Introduce el id del producto a consultar: "))
            product = find_product_by_id(prodId)
            print('Producto encontrado: ', product) if product else print('No se ha encontrado el producto: ', prodId)

        elif action == 2:  # Consultar todos los productos
            products = find_all_products()
            print('Hay un total de {} productos en base de datos: {}'.format(len(products), products))

        elif action == 3:  # Crear producto
            product = read_new_product_input()
            create_product(product)

        elif action == 4:  # Modificar producto
            product = read_product_input()
            update_product(product)

        elif action == 5:  # Borrar producto
            prodId = str(input("Introduce el id del producto a borrar: "))
            delete_product(prodId)

    except Exception as e:
        print(e)
