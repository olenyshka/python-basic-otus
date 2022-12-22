"""
create dataclass `Engine`
"""
from dataclasses import dataclass


# создайте датакласс Engine в модуле engine, добавьте атрибуты volume и pistons

@dataclass
class Engine:
    volume: float
    pistons: int


# Engine    Двигатель
# volume    объем
# pistons   поршни
