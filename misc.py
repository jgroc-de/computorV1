import re


def is_number(string: str) -> bool:
    try:
        float(string)

        return True
    except ValueError:
        return False


def is_single_variable(equation: str) -> dict:
    results = re.findall('([a-zA-Z] ?\^ ?\d)', equation)
    if results:
        print(results)
        for item in results:
            if item != results[0]:
                raise SyntaxError(
                    'String can not contains multiple variables like in 3 * X + 4 * Y + 2 * x (3 different variables)')
    else:
        raise SyntaxError('Invalid format')


def is_valid_string(equation: str):
    results = re.search('[^0-9*+-^a-zA-Z= ]+', equation)
    if results:
        raise SyntaxError(
            'String contains forbidden characters. Must be only [0-9]*+-X^=')


def is_empty(part: str):
    if len(part) == 0:
        raise SyntaxError('One part of the equation is empty')


def throw_exception_if_not_valid(equation: str):
    is_empty(equation)
    is_valid_string(equation)
    if equation.count('=') != 1:
        raise ValueError('More or less than ONE sign \'=\' in this equation')