class SmartPhone:
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model

class User:
    def __init__(self, first_name, last_name, smartphone):
        self.first_name = first_name
        self.last_name = last_name
        self.smartphone = smartphone


name = input("Introduce nombre de usuario")
lastname = input("Introduce apellido de usuario")
input("EL usuario tiene smartphone?")
manufacturer = input("Introduce fabricante de smartphone")
model = input("Introduce model de smartphone")
smartphone = SmartPhone(manufacturer, model)

user = User(name, lastname, smartphone)
