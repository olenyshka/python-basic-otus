"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*x):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in x]



# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

"""filter_numbers"""




def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
        return True




def filter_numbers(numbers, doparg):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if doparg == ODD:
        odds = list(filter(lambda x: x % 2 != 0, numbers))
        return odds
        #[number for number in numbers if number % 2 != 0]

    elif doparg == EVEN:
        evens = list(filter(lambda x: x % 2 == 0, numbers))
        return evens
        #[number for number in numbers if number % 2 == 0]

    elif doparg == PRIME:
        prim = list(filter(is_prime, numbers))


