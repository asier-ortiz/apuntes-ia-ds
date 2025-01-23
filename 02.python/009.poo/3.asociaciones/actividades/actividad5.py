"""
Actividad para la puesta en práctica del mecanismo de programación orientada a objetos 2.herencia y relación entre clases.

Crear la estructura de clases:

Infoproducto, con las siguientes características:

1) Atributos de instancia: precio

Autor, con las siguientes características:

1) Atributos de instancia: nombre, nif

Editorial, con las siguientes características:

1) Atributos de instancia: nombre, crowdfunding (boolean)

Profesor, con las siguientes características:

1) Atributos de instancia: nombre, email, url web

2 ) Método para verificar que el email es correcto antes de asignarlo en la creación de objetos de la clase profesor

Empresa, con las siguientes características:

1) Atributos de instancia: nombre, cif

Libro, con las siguientes características:

1) Atributos de instancia: isbn, título, género, autor (objeto), editorial (objeto)

Módulo, con las siguientes características:

1) Atributos de instancia: número, título, duración, categoría, lecciones (lista de textos)

Curso, con las siguientes características:

1) Atributos de instancia: título, categoría, profesor (objeto), empresa (objeto), lista de módulos (lista de objetos)

Destacamos como 2.herencia que tanto un curso como un libro heredan de
la clase infoproducto. El resto de clases tienen las relaciones que se
pueden ver en los atributos mencionados.

Una vez creada la estructura de clases crearemos objetos de cada una de ellas. Por ejemplo:

1 - Crear un autor, una editorial y un libro.

2 - Crear un profesor, una empresa, 4 listas de lecciones (listas de
elementos string), 4 módulos donde cada uno tiene una lista de
lecciones, un curso (el curso tiene asociado el profesor, la empresa, y
una lista con los 4 módulos)

Imprimiremos por consola cada objeto para verificar su representación textual.

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
    def __init__(self, precio, isbn, titulo, genero, autor, editorial):
        super().__init__(precio)
        self.isbn = isbn
        self.titulo = titulo
        self.genero = genero
        self.autor = autor
        self.editorial = editorial

    def __str__(self):
        return f"Libro(precio={self.precio}, " \
               f"isbn={self.isbn}, " \
               f"titulo={self.titulo}, " \
               f"genero={self.genero}, " \
               f"autor={self.autor}, " \
               f"editorial={self.editorial}" \
               f")"

    def __repr__(self):
        return self.__str__()


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


# CREACIÓN DE OBJETOS
# 1 - Crear un autor, una editorial y un libro.
autor_eckhart = Autor("Eckhart", "86743156T")
editorial_planeta = Editorial("Planeta", True)
libro1 = Libro(19.99, "123-45-6789-12", "El poder del ahora", "Espiritualidad", autor_eckhart, editorial_planeta)

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