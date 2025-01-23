import datetime
import mysql.connector as con


class Actor:
    def __init__(self, actor_id, first_name, last_name, last_update):
        self.actor_id = actor_id
        self.first_name = first_name
        self.last_name = last_name
        self.last_update = last_update


the_rock = Actor(202, "Dwayne", "Johnson", datetime.datetime.now())

database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin", database="sakila")
cursor = database.cursor()

sql = """
INSERT INTO actor (first_name, last_name)
VALUES (%s, %s);
"""
params = (the_rock.first_name, the_rock.last_name)
cursor.execute(sql, params)

database.commit()  # hace efectivos los cambios en base de datos

print(cursor.rowcount)

cursor.close()
database.close()
