"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, cargo=20, max_cargo=30, weight=3, fuel=30, fuel_consumption=2, started=True, dist=100):
        self.cargo = cargo
        self.max_cargo = max_cargo
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started
        self.dist = dist



    def load_cargo(self, dop_cargo: int):
        # try:
        #     dop_cargo + self.cargo <= self.max_cargo
        # except CargoOverload:
        #     print("перегруз")
        # else:
        #     self.cargo = dop_cargo + self.cargo
        #     return self.cargo
        if dop_cargo + self.cargo <= self.max_cargo:
            self.cargo = dop_cargo + self.cargo
            return self.cargo
        else:
            raise CargoOverload('перегруз')

    def remove_all_cargo(self):
        c = self.cargo
        self.cargo = 0
        return c

# в модуле plane создайте класс Plane
# класс Plane должен быть наследником Vehicle
# добавьте атрибуты cargo и max_cargo классу Plane
# добавьте max_cargo в инициализатор (переопределите родительский)
# объявите метод load_cargo, который принимает число, проверяет, что в сумме с текущим cargo не будет перегруза,
#                   и обновляет значение, в ином случае выкидывает исключение exceptions.CargoOverload
# объявите метод remove_all_cargo, который обнуляет значение cargo и возвращает значение cargo, которое было до обнуления
