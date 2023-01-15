"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption):        #, dist=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def set_engine(self, engine):
        self.engine = engine
        # self.volume = engine.volume
        # self.pistons = engine.pistons
        # return volume, pistons


# в модуле car создайте класс Car
# класс Car должен быть наследником Vehicle
# добавьте атрибут engine классу Car
# объявите метод set_engine, который принимает в себя экземпляр объекта Engine и устанавливает на текущий экземпляр Car






