from gg_math import equation_resolver
from print_output import gg_print
from parser import build_equation


def main(argv):
    number_of_args = len(argv)
    if number_of_args == 1:
        raise SyntaxError(
            'computorV1: equation is missing\n    ex: ./computorV1  "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"')
    elif number_of_args > 2:
        raise SyntaxError('too many arguments')
    # cas 0 = 0
    # throw_exception_if_not_valid(equation)
    equationParts = build_equation(argv[1].replace(' ', ''))
    result = equation_resolver.solve(equationParts[0], equationParts[1], equationParts[2])
    gg_print(equationParts, result)
