from src.solution.solutionFactory import SolutionFactory
from src.lexer.lexer import Lexer
from src.parser.parser import Parser
from src.calculus_type import basic, equation
from src.calculus_type.calculusTypeInterface import CalculusTypeInterface

class CalculusTypeFactory:
    def __init__(self):
        lexer = Lexer()
        parser = Parser()
        solutionFactory = SolutionFactory()
        self.__calculus_types = [
            basic.Basic(lexer, parser, solutionFactory),
            equation.Equation(lexer, parser, solutionFactory),
        ]

    def getCalculusType(self, calculus: str) -> CalculusTypeInterface:
        for calculus_type in self.__calculus_types:
            if calculus_type.can_compute_this(calculus):
                return calculus_type
        raise SyntaxError('cant compute this')     
