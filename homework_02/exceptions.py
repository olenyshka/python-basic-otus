"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


#
# raise LowFuelError(Exception)
# raise NotEnoughFuel(Exception)
# raise CargoOverload(Exception)

# class LowFuelError(Exception):
#     def __init__(self, text):
#         self.txt = text
#
# class NotEnoughFuel(Exception):
#     def __init__(self, text):
#         self.txt = text
#
# class CargoOverload(Exception):
#     def __init__(self, text):
#         self.txt = text

class LowFuelError(Exception):
    pass


class NotEnoughFuel(Exception):
    pass


class CargoOverload(Exception):
    pass
