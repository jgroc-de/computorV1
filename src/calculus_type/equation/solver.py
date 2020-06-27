from src.ft_math import ft_sqrt, ft_pow


def compute_delta(a: float, b: float, c: float) -> float:
    return ft_pow(b, 2) - 4 * a * c


def solution1(a: float, b: float, c: float, delta: float) -> float:
    return ((-b) - (ft_sqrt(delta))) / (2 * a)


def solution2(a: float, b: float, c: float, delta: float) -> float:
    return ((-b) + (ft_sqrt(delta))) / (2 * a)


def solver_degree_2(a: float, b: float, c: float) -> list:
    delta = compute_delta(a, b, c)
    if delta < 0:
        return []
    elif delta == 0:
        return [solution1(a, b, c, delta)]
    else:
        return [solution1(a, b, c, delta), solution2(a, b, c, delta)]


def solver_degree_2_case_0(b: float, c: float) -> list:
    if b == 0:
        return ['Any value of X can solve this equation, enjoy!']
    return [0, -b / c]


def solve(coef: list) -> list:
    a = 0
    b = 0
    c = 0
    if c != 0:
        if a == 0:
            return solver_degree_2_case_0(b, c)
        # manque un sqrt pour float
        return solver_degree_2(a, b, c)
    if b != 0:
        return [- a / b]
    if a != 0:
        return ["no value of X can solve this, sorry…"]
    return ["Any value of X can solve this equation, enjoy!"]