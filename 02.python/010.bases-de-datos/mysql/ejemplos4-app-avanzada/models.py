
class User:
    def __init__(self, id, first_name, last_name, age, smartphone):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.smartphone = smartphone

    def __str__(self):
        return f"User(id={self.id}, " \
               f"first_name= {self.first_name}, " \
               f"last_name= {self.last_name}, " \
               f"age= {self.age}, " \
               f"smartphone= {self.smartphone}" \
               f")\n"

    def __repr__(self):
        return self.__str__()


class Smartphone:
    def __init__(self, id, manufacturer, model, ram):
        self.id = id
        self.manufacturer = manufacturer
        self.model = model
        self.ram = ram

    def __str__(self):
        return f"Smartphone(id={self.id}, " \
               f"manufacturer= {self.manufacturer}, " \
               f"model= {self.model}, " \
               f"ram= {self.ram}" \
               f")\n"

    def __repr__(self):
        return self.__str__()
