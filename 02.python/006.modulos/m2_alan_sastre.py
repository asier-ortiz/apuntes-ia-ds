
laptops = []
sequence_id = 1

iterate = True
while iterate:

    print("""
Bienvenido/a a la tienda, selecciona una opción:
1 - Consultar ordenadores
2 - Consultar un ordenador 
3 - Crear un ordenador
4 - Actualizar un ordenador
    """)
    option = int(input(""))

    if option == 1:
        print("Listado de ordenadores:")
        print(laptops)
    elif option == 2:
        # Recolectar datos
        laptop_id = int(input("Introduce el id de ordenador:"))
        manufacturer = input("Introduce el fabricante:")
        model = input("Introduce el modelo de ordenador:")
        overclock = bool(input("Introduce si tiene overclock:"))

        # Crear ordenador
        # laptop = (laptop_id, )
        laptop1 = {
            "id": 1,
            "manufacturer": "",
            "model": ""
        }


        # Almacenar ordenador

    elif option == 6:
        iterate = False

