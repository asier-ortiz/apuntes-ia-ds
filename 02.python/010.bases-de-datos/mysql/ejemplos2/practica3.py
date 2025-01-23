class Engine:
    def __init__(self, cv, cc, model_engine):
        self.cv = cv
        self.cc = cc
        self.model_engine = model_engine

class Vehicle:
    def __init__(self, manufacturer, model, cv, cc, model_engine):
        self.manufacturer = manufacturer
        self.model = model
        self.engine = Engine(cv, cc, model_engine)  # Composicion


caballos = int(input("Introduce los Caballos del motor del coche: "))
vehicle = Vehicle("Ford", "Mondeo", 120, 1.2, "TDI")
vehicle.engine.cv = caballos