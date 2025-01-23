"""
Crear la clase Smartphone que represente un teléfono móvil inteligente. La clase debe contener:

- Atributos de clase: red, número de cámaras, tipo de pantalla,
estado(booleano que indicará True si el teléfono está encendido o False
si el teléfono está apagado)
- Atributos de instancia: id, pulgadas, resolución, altura, ancho,
peso, memoria ram, procesador, capacidad memoria, megapíxeles de cámara
- Método constructor
- Métodos: encender (cambia el atributo estado), apagar (cambia el
atributo estado), reiniciar, obtener número de notificaciones (devuelve
un número aleatorio)

A mayores, añadiremos el método string (método especial) que
permitirá obtener una representación textual de los objetos creados a
partir de esa clase.

Después crearemos diferentes objetos y modificaremos sus atributos y
ejecutaremos sus métodos, verificando que efecitvamente cambia su estado
 y al imprimirlos por consola se muestran todas sus propiedades.
"""
import datetime
import random


class Smartphone:
    # Atributos de clase
    network = "5G"
    num_cams = 2
    screen_type = "Amoled"
    status = False

    # Constructor
    def __init__(self, id, inches, resolution, height, width, weight, ram, cores, disk_mem, cam_mp):
        # Atributos de instancia
        self.id = id
        self.inches = inches
        self.resolution = resolution
        self.height = height
        self.width = width
        self.weight = weight
        self.ram = ram
        self.cores = cores
        self.disk_mem = disk_mem
        self.cam_mp = cam_mp
        self.creation_date = datetime.datetime.now()

    # Métodos (comportamiento): encender, apagar, reiniciar, get_notificationes
    def turn_on(self):
        self.status = True
        print("Se ha encendido el teléfono {}".format(self.id))

    def turn_off(self):
        self.status = False

    def restart(self):
        # self.status = False
        # self.status = True
        self.turn_off()
        self.turn_on()

    def get_notifications(self):
        return random.randint(0, 30)

    def __str__(self):
        """
        Método especial para obtener una representación textual del objeto
        :return:
        """
        return f"Smartphone(network={self.network}, " \
               f"num_cams= {self.num_cams}, " \
               f"screen_type= {self.screen_type}, " \
               f"status= {self.status}, " \
               f"id= {self.id}, " \
               f"inches= {self.inches}, " \
               f"resolution= {self.resolution}, " \
               f"height= {self.height}, " \
               f"creation_date= {self.creation_date}" \
               f")"

    def __repr__(self):
        return self.__str__()


one_plus = Smartphone(1, 4.3, 1080, 11, 8, 0.4, 8, 4, 120, 48)
iphone = Smartphone(2, 5.3, 1080, 11, 12, 0.4, 8, 4, 120, 48)
realme = Smartphone(3, 6.3, 1080, 11, 16, 0.4, 8, 8, 120, 48)

smartphones = [one_plus, iphone, realme]
print(smartphones)

for smartphone in smartphones:
    smartphone.turn_on()
    print(smartphone.get_notifications())

print(smartphones)

for smartphone in smartphones:
    smartphone.turn_off()
