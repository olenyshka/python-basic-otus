"""
create dataclass `Engine`
"""
from dataclasses import dataclass


# создайте датакласс Engine в модуле engine, добавьте атрибуты volume и pistons

@dataclass
class Engine:
    volume: float = None
    pistons: int = None


# Engine    Двигатель
# volume    объем
# pistons   поршни
