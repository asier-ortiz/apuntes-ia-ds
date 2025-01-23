# Operaciones base de datos

https://dev.mysql.com/doc/refman/8.0/en/

## Operaciones CRUD

* CREATE, RETRIEVE, UPDATE, DELETE


* Create: Insertar nuevos datos
``` 
INSERT INTO customer (store_id, first_name, last_name, email, address_id, active)
VALUES (%s, %s, %s, %s, %s, %s);
```
* Retrieve: Recuperar datos
    * Recuperar todos
    * Recuperar todos con proyecciones (solo determinadas columnas)
    * Recuperar un solo elemento por su clave primaria (customer_id)
    * Recuperar por orden (ORDER BY)
    * Recuperar con paginación (LIMIT 10, 30)
    * Recuperar de varias tablas
```
SELECT * FROM film_text
WHERE description like = '%MySQL%'
```
* Update: Actualizar datos
```
UPDATE customer
SET email = %s
WHERE customer_id = %s;
```

* Delete: Borrar datos
```
DELETE FROM customer 
WHERE customer_id = %s; 
```

## Sentencias DDL

* Crear base de datos
* Crear tabla
* Borrar tabla
* Borrar base de datos