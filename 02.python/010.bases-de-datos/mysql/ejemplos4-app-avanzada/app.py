import user_dao
import schema

schema.init_schema_execute_multi()
schema.load_data()

while True:
    print(
        """
1 - Consultar usuarios
2 - Consultar usuario por id
3 - Crear nuevo usuario
4 - Editar usuario existente
5 - Borrar un usuario por id
6 - Borrar todos los usuarios
7 - Salir
        """
    )
    option = int(input("Introduce una opción: \n"))
    if option == 1:  # 1 - Consultar usuarios
        users = user_dao.find_all()
        print("Listado de usuarios en base de datos:")
        print(users)

    elif option == 2:  # 2 - Consultar usuario por id
        id_user = int(input("Introduce el id de usuario:"))
        user = user_dao.find_one(id_user)
        if user is not None:
            print("El usuario encontrado es:")
            print(user)
        else:
            print("El usuario solicitado no existe")

    elif option == 3:  # 3 - Crear nuevo usuario
        user = user_dao.input_new()
        check = user_dao.create(user)
        if check:
            print("Usuario creado correctamente")

    elif option == 4:  # 4 - Editar usuario existente
        user = user_dao.input_update()
        check = user_dao.update(user)
        if check:
            print("Usuario modificado correctamente")
        else:
            print("No se ha podido modificar el usuario")

    elif option == 5:  # 5 - Borrar un usuario por id
        id_user = int(input("Introduce el id de usuario:"))
        check = user_dao.delete_one(id_user)
        if check:
            print("Usuario borrado correctamente ")
        else:
            print("No se ha podido borrar el usuario")

    elif option == 6:  # 6 - Borrar todos los usuarios
        print("Esto borrará todos los usuarios de la base de datos.")
        confirm = bool(int(input("¿Está seguro de que quiere borrar todos? (1 Yes, 0 No)")))
        if not confirm:
            continue

        user_dao.delete_all()
        print("Usuarios borrados correctamente")

    elif option == 7:  # 7 - Salir
        break

print("Hasta la próxima amigos, y recuerden no olviden poner a salvo sus bases de datos.")
