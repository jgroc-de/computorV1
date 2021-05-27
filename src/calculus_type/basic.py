from src.solution.solutionFactory import SolutionFactory
from src.solution.solutionInterface import SolutionInterface
from .calculusTypeInterface import CalculusTypeInterface
from src.lexer.lexer import Lexer
from src.parser.parser import Parser


class Basic(CalculusTypeInterface):
    def __init__(self, lexer: Lexer, parser: Parser, solutionFactory: SolutionFactory):
        self.__lexer = lexer
        self.__parser = parser
        self.__solutionFactory = solutionFactory

    def can_compute_this(self, calculus: str) -> bool:
        return calculus.find('=') == -1

    def compute(self, calculus: str) -> SolutionInterface:
        tokens = self.__lexer.tokenize(calculus)
        if len(tokens) == 0:
            raise ValueError('lexer error')
        result = self.__parser.parse_recursive(tokens, True)
        if len(tokens) != 0:
            self.__parser.set_error(tokens[0].error, tokens, False)
            raise ValueError('parser error')

        return self.__solutionFactory.getSolution(result)
