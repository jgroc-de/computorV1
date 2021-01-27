from .degreX import DegreX
from src.ft_math import ft_sqrt, ft_pow


class Degre2(DegreX):
    SHORT = ")) / "
    solution = []
    delta = 0
    is_imaginaire = False

    def __init__(self, equation: list):
        DegreX.__init__(self, equation)
        if len(equation) != 3:
            raise ValueError('too much params for degre 2')

    def solve(self):
        self.solution = self.__solve(
            self.equation[2], self.equation[1], self.equation[0])

    def compute_delta(self, degre2: float, degre1: float, degre0: float) -> float:
        return ft_pow(degre1, 2) - 4 * degre2 * degre0

    def solution1(self, degre2: float, degre1: float, delta: float) -> float:
        return ((-degre1) - (ft_sqrt(delta))) / (2 * degre2)

    def solution2(self, degre2: float, degre1: float, delta: float) -> float:
        return ((-degre1) + (ft_sqrt(delta))) / (2 * degre2)

    def solver_degree_2(self, degre2: float, degre1: float, degre0: float) -> list:
        if self.delta < 0:
            self.is_imaginaire = True
            return [0]
        else:
            return [self.solution1(degre2, degre1, self.delta), self.solution2(degre2, degre1, self.delta)]

    def __solve(self, degre2: float, degre1: float, degre0: float) -> list:
        self.delta = self.compute_delta(degre2, degre1, degre0)
        if degre1 == 0 and degre0 == 0:
            return []
        if degre0 == 0:
            return [0, -degre1 / degre2]
        return self.solver_degree_2(degre2, degre1, degre0)

    def to_string(self) -> str:
        discriminant = self.__get_discriminant()
        if len(self.solution) == 0:
            return discriminant
        text1 = '\n\tX1 = {}'
        text2 = '\n\tX2 = {}'
        return discriminant + text1.format(self.__get_solution1()) + text2.format(self.__get_solution2())

    def __get_discriminant(self) -> str:
        if self.delta > 0:
            return "Discriminant is strictly positive, the two solutions are:"
        if self.delta == 0:
            if len(self.solution) == 0:
                return "Discriminant is null and any value for X will do the job, Enjoy!"
            else:
                return "Discriminant is null, the two (same) solutions are:"
        if self.delta < 0:
            return "Discriminant is strictly negative, the two (imaginary) solutions are:"

    def __get_solution1(self) -> str:
        if self.is_imaginaire == True:
            result = "(" + str(-self.equation[1]) + " + i * sqrt(" + \
                str(self.delta) + self.SHORT + str(2 * self.equation[2])
        else:
            result = "(" + str(-self.equation[1]) + " + sqrt(" + \
                str(self.delta) + self.SHORT + str(2 * self.equation[2])
            result += " (or approx. " + str(round(self.solution[1], 6)) + ")"
        return result

    def __get_solution2(self) -> str:

        if self.is_imaginaire == True:
            result = "(" + str(-self.equation[1]) + " - i * sqrt(" + \
                str(self.delta) + self.SHORT + str(2 * self.equation[2])
        else:
            result = "(" + str(-self.equation[1]) + " - sqrt(" + \
                str(self.delta) + self.SHORT + str(2 * self.equation[2])
            result += " (or approx. " + str(round(self.solution[0], 6)) + ")"
        return result
