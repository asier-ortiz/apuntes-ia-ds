"""
Partiendo de la solución aportada en la actividad 5 realizar:

1. Sobrecarga de operadores

Añadir métodos que definan el comportamiento para las siguiente acciones sobre operaciones con módulos:

Método operador suma: cuando se suman dos módulos lo que se hace es sumar su duración

Método resta: cuando se restan dos módulos lo que se hace es restar su duración

Método igual: cuando se comparan dos módulos lo que se hace es comparar su duración

Método menor que: cuando se comparan dos módulos lo que se hace es comparar su duración

Método mayor que: cuando se comparan dos módulos lo que se hace es comparar su duración

Agregaremos estos métodos sobre la clase Módulo, y
depsués crearemos objetos de esta clase y utilizaremos los operadores
imprimiendo por consola el resultado de cada uno de ellos, por ejemplo :

module1 == module 2

module2 - module1

module2 > module1

etc

2. Polimorfismo

✅ Crear una nueva clase Capitulo (Chapter) que tenga un atributo paginas (int)

✅ Modificar la clase Libro para que contenga una lista de objetos capitulos

✅ Crear el método obtener longitud en las clases Libro y Curso

✅ El método obtener longitud de la clase Libro calculará la duración a partir de sumar el número de páginas de sus
capítulos, estos capítulos están en la lista de objetos nueva que hemos añadido como atributo de
instancia en la clase Libro.

✅ El método obtener longitud de la clase Curso calculará la duración a partir de sumar la duración de sus módulos,
el objeto módulo ya tenía un atributo duración por lo que solo tendremos que sumar los atributos
duracion de los módulos asociados a un curso.

Crear una función externa a las clases y que se llame obtener longitud que reciba un objeto libro o curso y que llame
al método obtener longitud de dichas clases para retornar la longitud total de ese infoproducto.

"""
# CREACIÓN DE CLASES


class InfoProducto:
    def __init__(self, precio):
        self.precio = precio

    def __str__(self):
        return f"InfoProducto(precio={self.precio}" \
               f")"

    def __repr__(self):
        return self.__str__()


class Autor:
    def __init__(self, nombre, nif):
        self.nombre = nombre
        self.nif = nif

    def __str__(self):
        return f"Autor(nombre={self.nombre}" \
               f"nif={self.nif} " \
               f")"

    def __repr__(self):
        return self.__str__()


class Editorial:
    def __init__(self, nombre, crowdfunding):
        self.nombre = nombre
        self.crowdfunding = bool(crowdfunding)

    def __str__(self):
        return f"Editorial(nombre={self.nombre}, " \
               f"crowdfunding={self.crowdfunding}, " \
               f")"

    def __repr__(self):
        return self.__str__()


class Profesor:
    def __init__(self, nombre, email, url_web):
        self.nombre = nombre
        self.email = self.__validate_email(email)
        self.url_web = url_web

    def __validate_email(self, email):  # Comprobar que contiene @ y punto .
        # Opción 1 - Comprobar @ y punto
        # if "@" in email and "." in email:
        #     return email
        # else:
        #     return ""
        return email if "@" in email and "." in email else ""
        # Opción 2 - expresión regular

    def __str__(self):
        return f"Profesor(nombre={self.nombre}, " \
               f"email={self.email}, " \
               f"url_web={self.url_web}" \
               f")"

    def __repr__(self):
        return self.__str__()


class Empresa:
    def __init__(self, nombre, cif):
        self.nombre = nombre
        self.cif = cif

    def __str__(self):
        return f"Empresa(nombre={self.nombre}, " \
               f"cif={self.cif}" \
               f")"

    def __repr__(self):
        return self.__str__()


class Libro(InfoProducto):
    def __init__(self, precio, isbn, titulo, genero, autor, editorial, capitulos):
        super().__init__(precio)
        self.isbn = isbn
        self.titulo = titulo
        self.genero = genero
        self.autor = autor
        self.editorial = editorial
        self.capitulos = capitulos

    def __str__(self):
        return f"Libro(precio={self.precio}, " \
               f"isbn={self.isbn}, " \
               f"titulo={self.titulo}, " \
               f"genero={self.genero}, " \
               f"autor={self.autor}, " \
               f"editorial={self.editorial}, " \
               f"capitulos={self.capitulos}" \
               f")"

    def __repr__(self):
        return self.__str__()

    def obtener_longitud(self):
        # Obtener longitud en base a el número de páginas de cada capítulo
        longitud = 0
        for capitulo in self.capitulos:
            longitud += capitulo.num_paginas
        return longitud


class Modulo:
    def __init__(self, numero, titulo, duracion, categoria, lecciones):
        self.numero = numero
        self.titulo = titulo
        self.duracion = duracion
        self.categoria = categoria
        self.lecciones = lecciones

    def __str__(self):
        return f"Modulo(numero={self.numero}, " \
               f"titulo={self.titulo}, " \
               f"duracion={self.duracion}, " \
               f"categoria={self.categoria}, " \
               f"lecciones={self.lecciones}" \
               f")\n"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return self.duracion + other.duracion

    def __sub__(self, other):
        result = self.duracion - other.duracion
        return result if result >= 0 else 0

    def __eq__(self, other):
        return self.duracion == other.duracion

    # def __gt__(self, other): # Equivale a >
    def __ge__(self, other):  # Equivale a >=
        return self.duracion >= other.duracion




class Curso(InfoProducto):
    def __init__(self, precio, titulo, categoria, profesor, empresa, modulos):
        super().__init__(precio)
        self.titulo = titulo
        self.categoria = categoria
        self.profesor = profesor
        self.empresa = empresa
        self.modulos = modulos

    def __str__(self):
        return f"Curso(precio={self.precio}, " \
               f"titulo={self.titulo}, " \
               f"categoria={self.categoria}, " \
               f"profesor={self.profesor}, " \
               f"empresa={self.empresa}, " \
               f"6.modulos={self.modulos} \n" \
               f")"

    def __repr__(self):
        return self.__str__()

    def obtener_longitud(self):
        duracion_total = 0
        for modulo in self.modulos:
            duracion_total += modulo.duracion
        return duracion_total


class Capitulo:
    def __init__(self, num_paginas):
        self.num_paginas = num_paginas


def len_info_producto(info_producto):
    return info_producto.obtener_longitud()


# CREACIÓN DE OBJETOS
# 1 - Crear un autor, una editorial y un libro.
autor_eckhart = Autor("Eckhart", "86743156T")
editorial_planeta = Editorial("Planeta", True)
chapter1 = Capitulo(100)
chapter2 = Capitulo(120)
chapter3 = Capitulo(115)
chapters = [chapter1, chapter2, chapter3]
libro1 = Libro(19.99, "123-45-6789-12", "El poder del ahora", "Espiritualidad", autor_eckhart,
               editorial_planeta, chapters)

# Crear un profesor, una empresa, 4 listas de lecciones (listas de
# elementos string), 4 módulos donde cada uno tiene una lista de
# lecciones, un curso (el curso tiene asociado el profesor, la empresa, y
# una lista con los 4 módulos)

profesor = Profesor("Juancito", "juancitoexample.com", "https://www.juancito3000.com")
empresa = Empresa("DESARROLLOS COSMICOS SL", "B3344556")

modulo1_lecciones = ["HTML", "CSS", "JS", "BOOTSTRAP", "GIT", "GITHUB", "JQUERY", "VSCODE"]
modulo2_lecciones = ["FUNDAMENTOS", "SINTAXIS", "FUNCIONES", "ESTRUCTURAS DATOS", "ESTRUCTURAS CONTROL",
                     "MÓDULOS Y PAQUETES", "EXCEPCIONES", "PYCHARM"]
modulo3_lecciones = ["CLASES", "OBJETOS", "ENCAPSULACIÓN", "HERENCIA", "POLIMORFISMO", "ASOCIACIONES",
                     "SOBRE ESCRITURA", "SOBRECARGA"]
modulo4_lecciones = ["BASES DE DATOS", "MYSQL", "MONGODB"]
modulo5_lecciones = ["FRAMEWORKS WEB", "DJANGO", "FLASK"]
modulo6_lecciones = ["NUMPY", "PANDAS", "MATPLOTLIB", "SEABORN", "SCIKIT LEARN"]

modulo1 = Modulo(1, "Tecnologías Frontend", 14, "Frontend", modulo1_lecciones)
modulo2 = Modulo(2, "Sintaxis Python", 7, "Backend", modulo2_lecciones)
modulo3 = Modulo(3, "Programación Orientada a Objetos", 7, "Backend", modulo3_lecciones)
modulo4 = Modulo(4, "Acceso a bases de datos", 7, "Bases de datos", modulo4_lecciones)
modulo5 = Modulo(5, "Frameworks web", 14, "Web", modulo5_lecciones)
modulo6 = Modulo(6, "Ciencia de datos", 7, "Datos", modulo6_lecciones)

python_modulos = [modulo1, modulo2, modulo3, modulo4, modulo5, modulo6]

curso_python = Curso(0, "Desarrollo web con Python", "Programación", profesor, empresa, python_modulos)
print(curso_python)

# SOBRECARGA DE OPERADORES

# OPERADOR SUMA
duracion_m1_m2 = modulo1 + modulo2
print("duración m1({}) + m2({}) = {}".format(modulo1.duracion, modulo2.duracion, duracion_m1_m2))

# OPERADOR RESTA
duracion_m1_minus_m2 = modulo1 - modulo2
duracion_m2_minus_m1 = modulo2 - modulo1
print("duración m1({}) - m2({}) = {}".format(modulo1.duracion, modulo2.duracion, duracion_m1_minus_m2))
print("duración m2({}) - m1({}) = {}".format(modulo2.duracion, modulo1.duracion, duracion_m2_minus_m1))

# OPERADOR IGUAL
check_equals_m1_m2 = modulo1 == modulo2
check_equals_m2_m3 = modulo2 == modulo3
print("iguales m1({}) == m2({}) = {}".format(modulo1.duracion, modulo2.duracion, check_equals_m1_m2))
print("iguales m2({}) == m3({}) = {}".format(modulo2.duracion, modulo3.duracion, check_equals_m2_m3))

# Operador >=
ge_m1_m2 = modulo1 >= modulo2
ge_m2_m1 = modulo2 >= modulo1
print("mayor que m1({}) >= m2({}) = {}".format(modulo1.duracion, modulo2.duracion, ge_m1_m2))
print("mayor que m2({}) >= m1({}) = {}".format(modulo2.duracion, modulo1.duracion, ge_m2_m1))

## POLIMORFISMO

print("len_info_producto CURSO", len_info_producto(curso_python))  # Devuelve la longitud en base a la duración de los módulos en días
print("len_info_producto LIBRO", len_info_producto(libro1))  # Devuelve la longitud en base al número de páginas total de sus capítulos