
sql_retrieve_all = """
SELECT * FROM staff;
"""

sql_retrieve_one = """
SELECT * FROM staff
WHERE staff_id = %s;
"""

sql_insert = """
INSERT INTO staff (first_name, last_name, address_id, email, store_id, active, username, password)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
"""

sql_exists = """
SELECT 1 FROM sakila.staff 
WHERE staff_id = %s;
"""

sql_update = """
UPDATE staff
SET first_name = %s, last_name = %s, address_id = %s, email = %s, store_id = %s, active = %s, 
username = %s, password = %s
WHERE staff_id = %s;
"""

sql_delete_one = """
DELETE FROM staff
WHERE staff_id = %s;
"""

sql_delete_all = """
TRUNCATE TABLE staff;
"""