from gg_math.ft_sqrt import ft_sqrt


def compute_delta(a: float, b: float, c: float) -> float:
    return pow(b, 2) - 4 * a * c


def solution1(a: float, b: float, c: float, delta: float) -> float:
    return (-b - ft_sqrt(delta)) / (2 * a)


def solution2(a: float, b: float, c: float, delta: float) -> float:
    return (- b + ft_sqrt(delta)) / (2 * a)


def solver_degree_2(a: float, b: float, c: float) -> list:
    delta = compute_delta(a, b, c)
    if delta < 0:
        return []
    elif delta == 0:
        return [solution1(a, b, c, delta)]
    else:
        return [solution1(a, b, c, delta), solution2(a, b, c, delta)]


def solve(a: float, b: float, c: float) -> list:
    if c != 0:
        # manque un sqrt pour float
        return solver_degree_2(a, b, c)
    if b != 0:
        return [- a / b]
    raise ValueError('Equation of degree 0: nothing to solve')
