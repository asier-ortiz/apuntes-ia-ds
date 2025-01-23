
import mysql.connector as con
from sql import *
from models import User, Smartphone
from smartphone_dao import create_smartphone


def find_all():
    database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="mysqlapp")
    cursor = database.cursor()

    cursor.execute(sql_select_users)

    rows = cursor.fetchall()

    users = []
    for row in rows:
        if row[4] is not None:
            smartphone = Smartphone(row[4], None, None, None)
        else:
            smartphone = None
        user = User(row[0], row[1], row[2], row[3], smartphone)
        users.append(user)
    cursor.close()
    database.close()
    return users


def find_one(id_user):
    database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="mysqlapp")
    cursor = database.cursor()

    params = (id_user,)
    cursor.execute(sql_select_user, params)

    row = cursor.fetchone()
    cursor.close()
    database.close()

    if row is None:
        return None

    if row[4] is not None:
        smartphone = Smartphone(row[4], None, None, None)
    else:
        smartphone = None
    user = User(row[0], row[1], row[2], row[3], smartphone)

    return user


def input_new():
    print("A continuación introduzca los datos del nuevo usuario a crear:")
    first_name = input("Introduce Nombre: ")
    last_name = input("Introduce Apellido: ")
    age = int(input("Introduce Edad: "))

    has_smartphone = bool(int(input("¿El usuario tiene Smartphone? (0 - No, 1 - Sí)")))
    if has_smartphone:
        manufacturer = input("Introduce Fabricante: ")
        model = input("Introduce Modelo: ")
        ram = int(input("Introduce RAM: "))
        smartphone = Smartphone(None, manufacturer, model, ram)
    else:
        smartphone = None

    return User(None, first_name, last_name, age, smartphone)


def input_update():
    id_user = int(input("A continuación introduzca el id del usuario que desea editar:"))
    if not exists(id_user):
        print("El usuario solicitado no existe")
        return None

    first_name = input("Introduce Nombre: ")
    last_name = input("Introduce Apellido: ")
    age = int(input("Introduce Edad: "))

    return User(id_user, first_name, last_name, age, None)


def exists(id_user):
    if id_user is None:
        return False

    database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="mysqlapp")
    cursor = database.cursor()

    param_id = (id_user,)
    cursor.execute(sql_exists_user, param_id)
    result = cursor.fetchone()

    cursor.close()
    database.close()

    return bool(result)


def create(user):
    if user is None:
        return False

    database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="mysqlapp")
    cursor = database.cursor()

    id_smartphone = create_smartphone(user.smartphone)

    params = (
        user.first_name,
        user.last_name,
        user.age,
        id_smartphone
    )
    cursor.execute(sql_insert_user, params)
    database.commit()
    result_num = cursor.rowcount  # 1 usuario insertado
    cursor.close()
    database.close()
    return False if result_num == 0 else True


def update(user):
    if user is None:
        return False

    database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="mysqlapp")
    cursor = database.cursor()

    # TODO - Smartphone
        # 1. Se quiere agregar un smartphone (seleccionando de la lista actual de smartphones) nuevo al usuario (30')
        # 2. Se quiere crear un nuevo smartphone y agregarlo al usuario (1h)
        # 2. Actualizar el smartphone que ya tiene (30')
        # 3. Desasociar el smartphone que ya tiene (pasar la columna a NULL) (30')

    params = (
        user.first_name,
        user.last_name,
        user.age,
        user.id
    )
    cursor.execute(sql_update_user, params)
    database.commit()
    result_num = cursor.rowcount  # 1 usuario modificado
    cursor.close()
    database.close()
    return False if result_num == 0 else True


def delete_one(id_user):
    if not exists(id_user):
        print("El usuario solicitado no existe")
        return False

    database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="mysqlapp")
    cursor = database.cursor()

    params = (id_user,)
    cursor.execute(sql_delete_user, params)
    database.commit()
    result_num = cursor.rowcount  # 1 usuario eliminado
    cursor.close()
    database.close()
    return False if result_num == 0 else True


def delete_all():
    database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="mysqlapp")
    cursor = database.cursor()
    cursor.execute(sql_delete_users)
    cursor.close()
    database.close()
