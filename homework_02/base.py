from abc import ABC


from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    # weight = None
    # started = None
    # fuel = None
    # fuel_consumption = None
    # new_fuel = None

    def __init__(self, started=None, weight=None, fuel=None, fuel_consumption=None, dist=None):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started
        self.dist = dist

    # добавьте атрибуты weight, started, fuel, fuel_consumption со значениями по умолчанию
    # добавьте инициализатор для установки weight, fuel, fuel_consumption

    def start(self, started):
        if started is False:
            if self.fuel > 0:
                started = True
                return started
            else:
                raise LowFuelError


    def move(self, dist):
        if (self.fuel - self.dist * self.fuel_consumption) >= 0:
            self.fuel = self.fuel - self.dist * self.fuel_consumption
            return self.fuel
        else:
            raise NotEnoughFuel



# добавьте метод start. При вызове этого метода необходимо проверить состояние started.
# И если не started, то нужно проверить, что топлива больше нуля, и обновить состояние started,
# иначе нужно выкинуть исключение exceptions.LowFuelError


# добавьте метод move, который проверяет,
# что топлива достаточно для преодоления переданной дистанции (вплоть до полного расхода),
# и изменяет количество оставшегося топлива, иначе выкидывает исключение exceptions.NotEnoughFuel


