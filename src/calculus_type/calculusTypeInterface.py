from src.lexer.lexer import Lexer
from src.parser.parser import Parser

class CalculusTypeInterface():
    def __init__(self, lexer: Lexer, parser: Parser):
        pass

    def can_compute_this(self, calculus: str) -> bool:
        ''' Define if can compute this or not '''
        pass

    def compute(self, calculus: str):
        ''' Compute the required calculus '''
        pass
