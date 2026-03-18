class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print("Марка:", self.brand)
        print("Модель:", self.model)
        print("Год:", self.year)


class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        Vehicle.__init__(self, brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        Vehicle.display_info(self)
        print("Дверей:", self.num_doors)


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        Vehicle.__init__(self, brand, model, year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        Vehicle.display_info(self)
        print("Коляска:", self.has_sidecar)


car = Car("BMw", "x5", 2021, 4)
motorcycle = Motorcycle("Toyota", "Land Cruiser", 2021, False)

print("Машина:")
car.display_info()

print("\nМотоцикл:")
motorcycle.display_info()
