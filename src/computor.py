from src.computor_src import lexer, parser


def compute(calculus: str) -> float:
    calculus_parts = calculus.split('=')
    if len(calculus_parts) == 1:
        tokens = lexer.tokenize(calculus)
        if len(tokens) == 0:
            raise ValueError('error')
        result = parser.parse_recursive(tokens)

        return result
    elif len(calculus_parts) == 2:
        if len(calculus_parts[0]) == 0 or len(calculus_parts[1]) == 0:
            raise SyntaxError('one part of the equation is empty')
        pass
    else:
        raise SyntaxError('too many sign =')