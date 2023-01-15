from abc import ABC


from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=3, fuel=40, fuel_consumption=2):        #, ):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        # self.started = started
        # self.dist = dist
        self.started = False

    # добавьте атрибуты weight, started, fuel, fuel_consumption со значениями по умолчанию
    # добавьте инициализатор для установки weight, fuel, fuel_consumption

    def start(self):
        if self.started is False:
            if self.fuel > 0:
                self.started = True
                # return self.started
            else:
                raise LowFuelError('не started')

    # добавьте метод start. При вызове этого метода необходимо проверить состояние started.
    # И если не started, то нужно проверить, что топлива больше нуля, и обновить состояние started,
    # иначе нужно выкинуть исключение exceptions.LowFuelError

    def move(self, dist):
        if (self.fuel - dist * self.fuel_consumption) >= 0:
            self.fuel = self.fuel - dist * self.fuel_consumption
            print(self.fuel)
            return self.fuel
        else:
            raise NotEnoughFuel('недостаточно топлива')

# vec = Vehicle(3, 40, 2)
#
# vec.move(10)




# добавьте метод move, который проверяет,
# что топлива достаточно для преодоления переданной дистанции (вплоть до полного расхода),
# и изменяет количество оставшегося топлива, иначе выкидывает исключение exceptions.NotEnoughFuel


