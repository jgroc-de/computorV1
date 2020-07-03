from .calculusInterface import CalculusInterface
from .basic_misc.lexer.lexer import Lexer
from .basic_misc.parser.parser import Parser

class Basic(CalculusInterface):
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()

    def can_compute_this(self, calculus: str) -> bool:
        if calculus.find('=') == -1:
            return True
        return False

    def compute(self, calculus: str, variables: list) -> float:
        tokens = self.lexer.tokenize(calculus, variables)
        if len(tokens) == 0:
            raise ValueError('lexer error')
        try:
            result = 0
            result = self.parser.parse_recursive(tokens, True)
            if len(tokens) != 0:
                self.parser.setError(tokens[0].error, tokens)
                raise ValueError('parser error')
        except ValueError:
            raise ValueError('parser error')

        return result
