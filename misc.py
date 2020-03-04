import re


def split_trim(string: str, splitter: str) -> list:
    parts = string.split(splitter)

    return [item.strip() for item in parts]


def is_number(string: str) -> bool:
    try:
        float(string)

        return True
    except ValueError:
        return False


def is_single_variable(equation: str) -> dict:
    results = re.findall('([a-zA-Z] ?\^ ?\d)', equation)
    if results:
        results = [item.replace(' ', '') for item in results]
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


def is_empty(part: str, item: str):
    if len(part) == 0:
        raise SyntaxError('{} part is empty'.format(item))


def throw_exception_if_not_valid(equation: str):
    if len(equation) == 0:
        raise SyntaxError('String is empty')
    is_valid_string(equation)
    if (equation.count('=') != 1):
        raise SyntaxError('second part is missing or too many =')
    parts = equation.split('=')
    is_empty(parts[0], 'first')
    is_empty(parts[1], 'second')
    is_single_variable(parts[0])
    is_single_variable(parts[1])
