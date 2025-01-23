
class Vehicle:

    num_ruedas = 2

    def __init__(self, id, manufacturer, model, price):
        self.id = id
        self.manufacturer = manufacturer
        self.model = model
        self.price = price

    def acelerar(self):
        print("Acelerando de 0 a 120")


class Car(Vehicle):
    pass


class MotorCycle(Vehicle):
    pass


class Tractor(Vehicle):
    def acelerar(self):  # Tractor sobreescribe el método acelerar()
        print("Cambiando de modo tortuga a modo liebre!")


class Monopatin():
    def __init__(self, brand):
        self.brand = brand

    def acelerar(self):
        print("Empujando con zancada")


car = Car(1, "Car", "Car", 999999)
motorcycle = MotorCycle(2, "MotorCycle", "MotorCycle", 999999)
tractor = Tractor(3, "Tractor", "Tractor", 999999)
monopatin = Monopatin("Monopatin SL")

vehicles = [car, motorcycle, tractor, monopatin]
for vehicle in vehicles:
    vehicle.acelerar()