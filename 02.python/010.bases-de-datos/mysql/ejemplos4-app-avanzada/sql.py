sql_select_users = "SELECT * FROM mysqlapp.USER;"

sql_select_user = "SELECT * FROM mysqlapp.USER WHERE id = %s;"

sql_insert_smartphone = """
INSERT INTO mysqlapp.SMARTPHONE (manufacturer, model, ram) 
VALUES (%s, %s, %s)
"""

sql_insert_user = """
INSERT INTO mysqlapp.USER (first_name, last_name, age, id_smartphone)
VALUES (%s, %s, %s, %s)
"""

sql_exists_user = """
SELECT 1 FROM mysqlapp.USER
WHERE id = %s;
"""

sql_update_user = """
UPDATE mysqlapp.USER
SET first_name = %s, last_name = %s, age = %s
WHERE id = %s;
"""

sql_delete_user = """
DELETE FROM mysqlapp.USER
WHERE id = %s;
"""

sql_delete_users = """
TRUNCATE TABLE mysqlapp.USER;
"""