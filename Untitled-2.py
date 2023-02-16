import itertools
from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления'
           ' квадратного корня из заданного числа')


def CalculateSquareRoot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Вычесляет твое число."""
    if your_number <= 0:
        return itertools(your_number)

    numbers = CalculateSquareRoot(your_number)

    print(
        f'Мы вычислили квадратный корень из введённого вами числа.'
        f' Это будет: {numbers}')


print(message)
calc(25.5)