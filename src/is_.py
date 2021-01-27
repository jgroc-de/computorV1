import re


def is_float(string: str) -> bool:
    try:
        float(string)

        return True
    except ValueError:
        return False


def is_valid_string(equation: str):
    results = re.search('[^0-9*+-^X= ]+', equation)
    if results:
        raise SyntaxError(
            'String contains forbidden characters. Must be only characters in [0-9]+-X^=')


def is_empty(part: str):
    if len(part) == 0:
        raise SyntaxError('One part of the equation is empty')


def count_equal(equation: str):
    if equation.count('=') > 1:
        raise ValueError('More than ONE sign \'=\' in this equation')


def is_number(test: str) -> bool:
    if test.isdigit() or test == '.':
        return True
    return False


def throw_exception_if_not_valid(equation: str):
    is_empty(equation)
    is_valid_string(equation)
    count_equal(equation)
