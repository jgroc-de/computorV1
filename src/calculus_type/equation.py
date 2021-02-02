from .calculusInterface import CalculusInterface
from .basic import Basic
from .equationType import degre0, degre1, degre2, degreX
from src.lexer.lexer import Lexer
from src.parser.parser import Parser


class Equation(CalculusInterface):
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()

    def can_compute_this(self, calculus: str) -> bool:
        if calculus.count('=') == 1:
            return True
        return False

    def compute(self, calculus: str) -> float:
        calculus_parts = calculus.split('=')
        if len(calculus_parts[0]) == 0 or len(calculus_parts[1]) == 0:
            raise ValueError('one part of the equation is empty')
        left_part = self.__parse_part(calculus_parts[0])
        right_part = self.__parse_part(calculus_parts[1])

        reducted_form = self.__add(left_part, right_part)
        reducted_form = self.__reduce(reducted_form)
        print(reducted_form)
        result = self.__solve(reducted_form)

        return result

    def __reduce(self, tab: list) -> list:
        while len(tab) > 1 and tab[len(tab)-1] == 0:
            tab.pop()
        return tab

    def __add(self, left_part: list, right_part: list) -> list:
        max_length = max(len(left_part), len(right_part))
        result = []
        for i in range(0, max_length):
            left = 0
            right = 0
            if len(left_part) > i:
                left = left_part[i]
            if len(right_part) > i:
                right = right_part[i]
            result.append(left - right)
        return result + [0, 0]

    def __parse_part(self, part: str):
        tokens = self.lexer.tokenize(part)
        part_by_degree = self.parser.cut_variables_bloc(tokens)
        result = []
        for degree_tokens in part_by_degree:
            if len(degree_tokens) == 0:
                result.append(0)
                continue
            result.append(self.parser.parse_recursive(degree_tokens, True))
            if len(degree_tokens) != 0:
                self.parser.set_error(
                    degree_tokens[0].error, degree_tokens, False)
                raise ValueError('parser error')
        return result

    def __solve(self, equation_parts: list) -> list:
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
