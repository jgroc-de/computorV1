from src.lexer.lexer import Lexer
from src.parser.parser import Parser


def compute(calculus: str) -> float:
    calculus_parts = calculus.split('=')
    my_lexer = Lexer()
    my_parser = Parser()
    result = 0
    if len(calculus_parts) == 1:
        tokens = my_lexer.tokenize(calculus)
        if len(tokens) == 0:
            raise ValueError('lexer error')
        try:
            result = my_parser.parse_recursive(tokens)
        except ValueError:
            raise ValueError('parser error')
    elif len(calculus_parts) == 2:
        if len(calculus_parts[0]) == 0 or len(calculus_parts[1]) == 0:
            raise SyntaxError('one part of the equation is empty')
        pass
    else:
        raise SyntaxError('too many sign =')

    result = round(result, 8)
    #for case -0.0
    if (result == 0):
        return 0.0
    return result