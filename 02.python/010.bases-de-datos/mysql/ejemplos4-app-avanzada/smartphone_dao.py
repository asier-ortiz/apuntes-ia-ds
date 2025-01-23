import mysql.connector as con
from sql import *


def create_smartphone(smartphone):
    if smartphone is None:
        return None

    database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="mysqlapp")
    cursor = database.cursor()

    params = (
        smartphone.manufacturer,
        smartphone.model,
        smartphone.ram,
    )
    cursor.execute(sql_insert_smartphone, params)
    database.commit()
    cursor.close()
    database.close()
    return cursor.lastrowid
