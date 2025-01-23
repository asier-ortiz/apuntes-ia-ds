import mysql.connector as con


def init_schema_execute():
    """
    Regenera la base de datos (comando a comando)
    """
    database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin")
    cursor = database.cursor()
    file = open("sql/schema.sql")
    sql_content = file.read()
    file.close()
    sql_content = sql_content.replace("\n", "").replace("\t", "")
    sql_sentences = sql_content.split(";")

    for sql in sql_sentences:
        if sql:
            cursor.execute(sql + ";")

    cursor.close()
    database.close()


def init_schema_execute_multi():
    """
    Regenera la base de datos (todos los comandos en una misma ejecución)
    """
    database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin")
    cursor = database.cursor()
    file = open("sql/schema.sql")
    sql_content = file.read()
    file.close()
    # cursor.execute(sql_content)
    cursor.execute(sql_content, multi=True)
    cursor.close()
    database.close()


def load_data():
    """
    Carga datos de prueba en la base de datos
    """
    database = con.connect(host="127.0.0.1", port="3300", user="root", password="admin")
    cursor = database.cursor()
    file = open("sql/data.sql")
    sql_content = file.read()
    file.close()
    sql_content = sql_content.replace("\n", "").replace("\t", "")
    sql_sentences = sql_content.split(";")

    for sql in sql_sentences:
        if sql:
            cursor.execute(sql + ";")
            database.commit()
    cursor.close()
    database.close()
