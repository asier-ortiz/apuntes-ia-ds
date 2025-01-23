"""
Actividad para la puesta en práctica del mecanismo de programación orientada a objetos **2.herencia**.

Crearemos la clase base Empleado con los siguientes elementos:

1) Atributos de instancia: nombre, nif, número de la seguridad social, salario

2) Métodos: método trabajar, simplemente imprime un texto por pantalla

3) Método especial string para su representación textual por consola

Crearemos la clase hija Mecánico que herede de Empleado con los siguientes elementos:

1) Atributos de instancia: coches reparados (boolean), conocimiento de motocicletas (boolean)

2) Métodos: método trabajar sobreescrito, beber cerveza, elevar un
coche. Estos métodos simplemente imprimen un texto diferente cada uno
por consola.

3) Método especial string para su representación textual por consola

Crearemos la clase hija Programador que herede de Empleado con los siguientes elementos:

1) Atributos de instancia: líneas de código programadas (int), número de bugs arreglados (int)

2) Métodos: método trabajar sobreescrito, beber café, arreglar un
bug. Estos métodos simplemente imprimen un texto diferente cada uno por
consola.

3) Método especial string para su representación textual por consola

Una vez creada la anterior estructura de clases, crearemos un objeto
de cada una de las clases (3 objetos en total) y verificamos que sus
métodos funcionan y al imprimir por consola se muestran tanto las
variables de cada objeto como las heredadas de la clase padre.

También podemos hacer uso del método isinstance para verificar la clase a la que pertenece cada objeto.
"""

class Empleado:
    def __init__(self, id, nombre, nif, nss, salario):
        self.id = id
        self.nombre = nombre
        self.nif = nif
        self.nss = nss
        self.salario = salario

    def trabajar(self):
        print("Realizando horas de trabajo asociadas a nss: " + self.nss)

    def __str__(self):
        return f"Empleado(id={self.id}, " \
               f"nombre= {self.nombre}, " \
               f"nif= {self.nif}, " \
               f"nss= {self.nss}, " \
               f"salario= {self.salario}" \
               f")"


class Mecanico(Empleado):

    def __init__(self, id, nombre, nif, nss, salario, coches_reparados, repara_motos):
        super().__init__(id, nombre, nif, nss, salario)
        self.coches_reparados = coches_reparados
        self.repara_motos = repara_motos

    def trabajar(self):
        print("Trucando carros")

    def beber_cerveza(self):
        print("Cargando depósito cerveza")

    def elevar_autos(self):
        print("Elevar auto")

    def __str__(self):
        return f"Mecanico(id={self.id}, " \
               f"nombre= {self.nombre}, " \
               f"nif= {self.nif}, " \
               f"nss= {self.nss}, " \
               f"salario= {self.salario}, " \
               f"coches_reparados= {self.coches_reparados}, " \
               f"repara_motos= {self.repara_motos}" \
               f")"


class Programador(Empleado):

    def __init__(self, id, nombre, nif, nss, salario, num_codelines, fixed_bugs):
        super().__init__(id, nombre, nif, nss, salario)
        self.num_codelines = num_codelines
        self.fixed_bugs = fixed_bugs

    def trabajar(self):
        print("Desarrollando software awesómico")

    def beber_cafe(self):
        print("Cargando depósito coffee")

    def arreglar_bugs(self):
        print("Fixing bugs")

    def __str__(self):
        return f"Programador(id={self.id}, " \
               f"nombre= {self.nombre}, " \
               f"nif= {self.nif}, " \
               f"nss= {self.nss}, " \
               f"salario= {self.salario}, " \
               f"num_codelines= {self.num_codelines}, " \
               f"fixed_bugs= {self.fixed_bugs}" \
               f")"


empleado = Empleado(1, "Empleado1", "7777666643D", "123456789123456789", 50000.0)
programador = Programador(1, "Empleado1", "7777666643D", "123456789123456789", 50000.0, 100000, 9)
mecanico = Mecanico(1, "Empleado1", "7777666643D", "123456789123456789", 50000.0, 1500, True)

print(empleado)
print(programador)
print(mecanico)

print(isinstance(programador, Programador))
print(isinstance(programador, Empleado))
print(isinstance(programador, Mecanico))

print(isinstance(mecanico, Programador))
print(isinstance(mecanico, Empleado))
print(isinstance(mecanico, Mecanico))

empleado.trabajar()
print("********** PROGRAMADOR ********** ")
programador.trabajar()
programador.arreglar_bugs()
programador.beber_cafe()
print("********** MECANICO ********** ")
mecanico.trabajar()
mecanico.beber_cerveza()
mecanico.elevar_autos()


