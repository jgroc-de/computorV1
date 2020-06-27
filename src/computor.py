from src.lexer.lexer import Lexer
from src.parser.parser import Parser
from src.calculus_type import basic, equation


calculus_types = [
    basic.Basic(),
    equation.Equation(),
]


def main(equation):
    try:
        result = compute(equation)
        print(result)
    except ValueError:
        pass
    except SyntaxError as error:
        print(error)


def compute(calculus: str) -> float:
    taken_in_charge = False
    try:
        for c_type in calculus_types:
            if c_type.can_compute_this(calculus):
                result = c_type.compute(calculus)
                taken_in_charge = True
    except ValueError:
        raise ValueError('compute error')

    if not taken_in_charge:
        raise SyntaxError('cant compute this')

    result = round(result, 8)
    #for case -0.0
    if (result == 0):
        return 0.0
    return result
