
"""

Plantilla

Aplicación CRUD, que lea datos de ordenadores por consola y los almacene en una estructura de datos. La aplicación ofrece las siguientes opciones:

1 – Consultar ordenadores: devuelve los ordenadores que tiene guardados en una estructura de datos.

2 – Consultar un ordenador: solicita el id del ordenador y en base a eso

3 – Crear un nuevo ordenador: pide los datos de un ordenador (id, fabricante, modelo, precio, RAM, peso)

4 – Editar un ordenador: pide el id del ordenador y después todos los datos para sobreescribir los que ya tenía para ese ordenador.

5 – Borrar un ordenador: pide el id del ordenador y lo borra de la estructura de datos.

6 – Salir: rompe el bucle y termina la aplicación.

"""


laptops = []  # Lista


def create_laptop():
    laptop = dict()
    laptop["id"] = int(input("Introduce el id del laptop: "))
    laptop["manufacturer"] = input("Introduce el manufacturer del laptop: ")
    laptops.append(laptop)
    print("Ordenador registrado satisfactoriamente")


def find_laptop(id_laptop):
    for laptop in laptops:
        if laptop["id"] == id_laptop:
            return laptop

while True:
    print("""
    Menú de opciones: 
    1 - Consultar ordenadores
    2 - Consultar un ordenador
    3 - Crear un nuevo ordenador
    4 - Editar un ordenador
    5 - Borrar un ordenador
    6 – Salir
    """)
    option = int(input("Selecciona una opción: "))
    if option == 1:  # 1 - Consultar ordenadores
        print(laptops)
    elif option == 2:  # 2 - Consultar un ordenador
        if len(laptops) == 0:
            print("No hay ordenadores disponibles")
            continue

        id_laptop = int(input("Introduce el id de ordenador a consultar: "))

        laptop = find_laptop(id_laptop)
        if laptop is not None:
            print(laptop)
        else:
            print("No se ha encontrado el ordenador solicitado.")


    elif option == 3:  # 3 - Crear un nuevo ordenador
        create_laptop()

    elif option == 4:
        print("Has elegido 2")
    elif option == 5:
        print("Has elegido 2")
    elif option == 6:
        break

print("fin")
