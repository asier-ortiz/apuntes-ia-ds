import mysql.connector as con

database = con.connect(
    host="localhost",
    port="3300",
    user="root",
    password="admin",
    database="sakila"
)

cursor = database.cursor()

sql = """
INSERT INTO actor (first_name, last_name) 
VALUES (%s, %s);
"""

params = ("Alan", "Sastre")
cursor.execute(sql, params)
database.commit()

cursor.close()
database.close()