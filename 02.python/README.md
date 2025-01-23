
Python

## TIPOS DE DATOS

boolean

number

string

None

Creación de variables

## OPERADORES

* Aritméticos
* Comparación
* Lógicos
* Membresia

## FUNCIONES

Son bloques de código reutilizables con un nombre que pueden ser invocadas desde cualquier parte del código o desde otros archivos.

Muy habitual que cuando se importa una librería externa como por ejemplo numpy, pandas, matplotlib, se utilicen sus funciones en nuestros programas para distintos casos:

* mostrar un gráfico
* Crear un array np.array()
* Crear DataFrame pd.DataFrame()


## ESTRUCTURAS DE CONTROL:

* if
* elif
* else

* match case

* for
* while

* break
* continue


## ESTRUCTURAS DE DATOS

Predefinidas de Python

* Listas: []
* Tuplas: ()
* Diccionarios: {}
* Conjuntos: {}

Estructuras de librerías externas:

* Numpy: np.array()
* Pandas: pd.DataFrame()


## OOP - CLASES Y OBJETOS

OOP - Object Oriented Programming

POO - Programación Orientada a Objetos

Es una forma de programar, un paradigma de programación que permite crear en el código los conceptos que tenemos en la realidad como por ejemplo:

* Ordenador
* CuentaBancaria
* Coche
* Casa
* Empresa
* Empleado

Las palabras reservadas que permiten crear clases y objetos:

* class

Una clase es como el plano de una casa

Cuando creamos una casa a partir de un plano estaríamos creando un objeto.

* Clases: estructuras con la palabra class que definen atributos y métodos
* Objetos: instancias específicas de una clase

Ejemplo:

class Telefono:
    pass
    # aquí se define los atributos y métodos que tendrán todos los teléfonos en común


iphone = Telefono()
one_plus = Telefono()
xiaomi = Telefono()

Ejemplo:

Clase sería como una especie de plantilla o molde, y los objetos serían como las figuras que creas con esa plantilla o molde.

* Vehiculo
* Coche
* CocheElectrico

tesla = CocheElectrico()

## PAQUETES Y MÓDULOS

El gestor de paquetes pip permite instalar paquetes.

Opción 1: Desde una consola y se ejecuta pip install nombre_paquete

Opción 2: Desde un notebook ipynb: ! pip install nombre_paquete