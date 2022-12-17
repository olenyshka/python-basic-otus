from abc import ABC


from homework.homework_02.exceptions import LowFuelError, NotEnoughFuel


# from homework.homework_02.exceptions import LowFuelError, NotEnoughFuel
# class LowFuelError(Exception):
#     pass
#
#
# class NotEnoughFuel(Exception):
#     pass
#
#
# class CargoOverload(Exception):
#     pass


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

            # try:
            #     self.fuel > 0
            # except LowFuelError:
            #     print("Низкий уровень топлива")
            # else:
            #     started = True
            #     return started

    def move(self, dist):
        if (self.fuel - self.dist * self.fuel_consumption) >= 0:
            self.fuel = self.fuel - self.dist * self.fuel_consumption
            return self.fuel
        else:
            raise NotEnoughFuel

        # try:
        #     (self.fuel - self.dist * self.fuel_consumption) >= 0
        # except exceptions.NotEnoughFuel:
        #     print("Недостаточно топлива")
        # else:
        #     self.fuel = self.fuel - self.dist * self.fuel_consumption
        #     return self.fuel



# добавьте метод start. При вызове этого метода необходимо проверить состояние started.
# И если не started, то нужно проверить, что топлива больше нуля, и обновить состояние started,
# иначе нужно выкинуть исключение exceptions.LowFuelError


# добавьте метод move, который проверяет,
# что топлива достаточно для преодоления переданной дистанции (вплоть до полного расхода),
# и изменяет количество оставшегося топлива, иначе выкидывает исключение exceptions.NotEnoughFuel


# fuel_consumption  потребление топлива
# fuel          топливо
# Low Fuel Error        Ошибка низкого уровня топлива


# vic = Vehicle(started=True, weight=15, fuel=25, fuel_consumption=0.14, dist=50)
# #
# # vic.fuel = 25
# # vic.fuel_consumption = 0.14       # если считаем расход на 1 км
# # vic.started = True
# # dist = 50
# #
# # print(move(dist))
#
# # vic.move(vic.dist)
# print(vic.move(vic.dist))
