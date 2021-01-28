from .calculusInterface import CalculusInterface
from src.lexer.lexer import Lexer
from src.parser.parser import Parser


class Basic(CalculusInterface):
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()

    def can_compute_this(self, calculus: str) -> bool:
        if calculus.find('=') == -1:
            return True
        return False

    def compute(self, calculus: str) -> float:
        tokens = self.lexer.tokenize(calculus)
        if len(tokens) == 0:
            raise ValueError('lexer error')
        try:
            result = 0
            result = self.parser.parse_recursive(tokens, True)
            if len(tokens) != 0:
                self.parser.set_error(tokens[0].error, tokens)
                raise ValueError('parser error')
        except ValueError:
            raise ValueError('parser error')

        return round(result, 8)
