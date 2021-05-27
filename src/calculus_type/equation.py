from src.solution.solutionFactory import SolutionFactory
from src.solution.solutionInterface import SolutionInterface
from .calculusTypeInterface import CalculusTypeInterface
from src.equationType.equationSolverFactory import EquationSolverFactory
from src.lexer.lexer import Lexer
from src.parser.parser import Parser


class Equation(CalculusTypeInterface):
    def __init__(self, lexer: Lexer, parser: Parser, solutionFactory: SolutionFactory):
        self.__lexer = lexer
        self.__parser = parser
        self.__solutionFactory = solutionFactory
        self.__solverFactory = EquationSolverFactory()

    def can_compute_this(self, calculus: str) -> bool:
        return calculus.count('=') == 1

    def compute(self, calculus: str) -> SolutionInterface:
        calculus_parts = calculus.split('=')
        if len(calculus_parts[0]) == 0 or len(calculus_parts[1]) == 0:
            raise ValueError('one part of the equation is empty')
        left_part = self.__parse_part(calculus_parts[0])
        right_part = self.__parse_part(calculus_parts[1])

        reducted_form = self.__add(left_part, right_part)
        reducted_form = self.__reduce(reducted_form)
        print(reducted_form)
        solver = self.__solverFactory.getSolver(reducted_form)

        return solver.solve()

    def __reduce(self, tab: list) -> list:
        while len(tab) > 1 and tab[len(tab) - 1] == 0:
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

    def __parse_part(self, part: str) -> list:
        tokens = self.__lexer.tokenize(part)
        part_by_degree = self.__parser.cut_variables_bloc(tokens)
        result = []
        for degree_tokens in part_by_degree:
            if len(degree_tokens) == 0:
                result.append(0)
                continue
            result.append(self.__parser.parse_recursive(degree_tokens, True))
            if len(degree_tokens) != 0:
                self.__parser.set_error(
                    degree_tokens[0].error, degree_tokens, False)
                raise ValueError('parser error')
        return result
