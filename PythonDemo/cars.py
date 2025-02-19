class Car:
    def __init__(self, make, model):
        self.make= make
        self.model = model

    def __repr__(self):
        print(f"{self.model} make by {self.make}")


class Garage:
    def __init__(self):
        self.cars = set()

    def __len__(self):
        return len(self.cars)

    def add_cars(self, car):
        self.cars.add(car)
        print(car)


ford = Car("Ford", "Gt310")
ford.__repr__()
g1 = Garage()
if isinstance(ford, Car):
    g1.add_cars(ford)
    g1.add_cars('NinjaH2R')
    print(g1.__len__())
else:
    print("error")
raise "invalid car type"

# try:
#     g1.add_cars('ford1')
# except TypeError:
#     print("this is some type error")