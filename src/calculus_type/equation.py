from .calculusInterface import CalculusInterface
from .basic import Basic
from .equationType import degre0, degre1, degre2, degreX


class Equation(CalculusInterface):
    def __init__(self):
        self.basic = Basic()

    def can_compute_this(self, calculus: str) -> bool:
        if calculus.count('=') == 1:
            return True
        return False

    def compute(self, calculus: str) -> float:
        calculus_parts = calculus.split('=')
        if len(calculus_parts[0]) == 0 or len(calculus_parts[1]) == 0:
            raise ValueError('one part of the equation is empty')
        reducted_form = []
        parts_by_degree = self.__parse_part(calculus_parts)
        for part in parts_by_degree:
            reducted_form.append(self.basic.compute(part))
        result = self.__solve(reducted_form)

        return result

    def extract_part(self, part, sign):
        degree_results = []
        degree_parts = self.__parse_part(part)
        for part2 in degree_parts:
            degree_results.append(self.basic.compute(part2))

    def __parse_part(self, calculus: str) -> list:
        return []

    def __solve(self, equation_parts: list) -> list:
        equation_parts = [1, 2, 1]
        if len(equation_parts) == 1:
            equation = degre0.Degre0(equation_parts)
        elif len(equation_parts) == 2:
            equation = degre1.Degre1(equation_parts)
        elif len(equation_parts) == 3:
            equation = degre2.Degre2(equation_parts)
        else:
            equation = degreX.DegreX(equation_parts)
        equation.solve()
        return equation
