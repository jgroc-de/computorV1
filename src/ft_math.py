from math import sqrt


def ft_sqrt(number):
    return sqrt(number)


def ft_linear(x: float, coef: list) -> float:
    return float(coef[0]) + float(coef[1]) * x


def ft_pow(number: float, power: int) -> float:
    powered_number = 1
    while power > 0:
        power -= 1
        powered_number *= number
    while power < 0:
        power += 1
        powered_number /= number

    return powered_number


def ft_abs(number: float) -> float:
    return number if (number > 0) else (-number)
