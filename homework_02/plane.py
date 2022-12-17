"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework.homework_02.base import Vehicle
from homework.homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    # cargo = 19
    # max_cargo = 24

    def __init__(self, cargo, max_cargo):
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, dop_cargo: int):
        try:
            self.dop_cargo + self.cargo <= self.max_cargo
        except CargoOverload:
            print("перегруз")
        else:
            self.cargo = self.dop_cargo + self.cargo
            return self.cargo

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
# cargo     груз
# max_cargo     максимальный груз
# Plane         Самолет
# load_cargo        загружать груз
# Cargo Overload        Перегрузка груза
# remove all cargo      удалить весь груз