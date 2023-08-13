from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def CalculateSquareRoot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Что-то лол."""
    if your_number <= 0:
        return
    print('Мы вычислили квадратный корень из введённого вами числа.')
    print(CalculateSquareRoot(your_number))


print(message)
calc(25.5)
