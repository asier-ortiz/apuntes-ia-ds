"""
1 - ATRIBUTOS ENCAPSULADOS

Partiendo de la solución aportada en la actividad 1 aplicaremos
encapsulación a los atributos de la clase smartphone: tipo de pantalla,
estado, memoria ram

Adaptaremos el código para que trabaje con esos atributos encapsulados.

2 - METODO ENCAPSULADO
Crearemos el método check_sim encapsulado, que será una comprobación
de si está la SIM insertada antes de encender el teléfono, esta
comprobación simplemente se realizar obteniendo un número aleatorio 0 o 1
 donde 0 será False y 1 será True lo que indicará que si es True el
teléfono podrá encenderse, mientras que si es False el teléfono no podrá
 encenderse y se mantendrá apagado.

Al método check_sim solo se le puede llamar desde el método encender teléfono.

3 - MÉTODO SETTER
Crearemos un nuevo método que permita cambiar la memoria ram, debido a
 que la ram ahora es un atributo encapsulado. Sólo se podrá cambiar la
ram si el número que se pretende asignar es mayor que 2, es decir, solo
se puede actualizar la RAM siempre y cuando sea mayor que 2 GB.

Una vez realizadas las modificaciones en la clase Smartphone
crearemos objetos y utilizaremos los nuevos métodos creados para
verificar que funcionan correctamente, imprimiendo por consola los
objetos.
"""
import datetime
import random


class Smartphone:
    # Atributos de clase
    network = "5G"
    num_cams = 2
    __screen_type = "Amoled"
    __status = False

    # Constructor
    def __init__(self, id, inches, resolution, height, width, weight, ram, cores, disk_mem, cam_mp):
        # Atributos de instancia
        self.id = id
        self.inches = inches
        self.resolution = resolution
        self.height = height
        self.width = width
        self.weight = weight
        self.__ram = ram
        self.cores = cores
        self.disk_mem = disk_mem
        self.cam_mp = cam_mp
        self.creation_date = datetime.datetime.now()

    # Métodos (comportamiento): encender, apagar, reiniciar, get_notificationes
    def turn_on(self):
        if self.__check_sim():
            self.__status = True
            print("Se ha encendido el teléfono {}".format(self.id))
        else:
            print("Obligatorio insertar SIM para encender el teléfono!")

    def turn_off(self):
        self.__status = False

    def restart(self):
        self.turn_off()
        self.turn_on()

    def get_notifications(self):
        return random.randint(0, 30)

    def __check_sim(self):
        return bool(random.randint(0, 1))

    def set_ram(self, ram):
        if self.__validate_ram(ram):
            self.__ram = ram
            print("Se ha modificado la RAM satisfactoriamente", ram)
        else:
            print("RAM debe ser mayor y múltiplo de 2")

    def __validate_ram(self, ram):
        return 2 < ram < 64 and ram % 2 == 0 and ram > self.__ram

    def __str__(self):
        return f"Smartphone(network={self.network}, " \
               f"num_cams= {self.num_cams}, " \
               f"screen_type= {self.__screen_type}, " \
               f"status= {self.__status}, " \
               f"RAM= {self.__ram}, " \
               f"id= {self.id}, " \
               f"inches= {self.inches}, " \
               f"resolution= {self.resolution}, " \
               f"height= {self.height}, " \
               f"creation_date= {self.creation_date}" \
               f")"

    def __repr__(self):
        return self.__str__()


# Crear datos
one_plus = Smartphone(1, 4.3, 1080, 11, 8, 0.4, 8, 4, 120, 48)

# check check_sim: ver que cambia
one_plus.restart()
one_plus.restart()
one_plus.restart()
one_plus.restart()
one_plus.restart()
one_plus.restart()

# check set_ram
print(one_plus)
one_plus.set_ram(1)
one_plus.set_ram(2)
one_plus.set_ram(3)
one_plus.set_ram(120)
one_plus.set_ram(32)

