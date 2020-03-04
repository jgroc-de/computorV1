#!/usr/bin/python3

import re
import sys
from gg_math import equation_resolver
from gg_print import print_output
from misc import split_trim, throw_exception_if_not_valid, is_number


def sort_members_by_power(parts: list, sign: int) -> dict:
    members_by_degree = {0: [0], 1: [0], 2: [0]}
    for part in parts:
        number = 1
        power = 0
        for item in part:
            if is_number(item):
                number *= float(item)
            else:
                tmp = item.split('^')
                if len(tmp):
                    power = int(tmp[1])
                    if power > 2:
                        raise ValueError(
                            'The polynomial degree is stricly greater than 2, I can\'t solve.')
                    elif power < 0:
                        raise ValueError('Negative power is not allowed')
        members_by_degree[power].append(number)

    members_by_degree = [sign * sum(members_by_degree[i]) for i in range(0, 3)]

    return members_by_degree


def buildEquation(equation: str) -> list:
    parts = equation.split('=')
    parts[0] = re.split('[+-]', parts[0])
    parts[1] = re.split('[+-]', parts[1])
    parts[0] = [split_trim(item, '*') for item in parts[0]]
    parts[1] = [split_trim(item, '*') for item in parts[1]]
    left_members_by_degree = sort_members_by_power(parts[0], 1)
    right_members_by_degree = sort_members_by_power(parts[1], -1)
    parts = [
        left_members_by_degree[i] + right_members_by_degree[i]
        for i in range(0, 3)
    ]
    return parts


def main(argv):
    number_of_args = len(argv)
    if number_of_args == 1:
        raise SyntaxError(
            'computorV1: equation is missing\n    ex: ./computorV1  "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"')
    elif number_of_args > 2:
        raise SyntaxError('too many arguments')
    equation = argv[1]
    # cas 0 = 0
    # throw_exception_if_not_valid(equation)
    parts = buildEquation(equation)
    print(parts)
    result = equation_resolver.solve(parts[0], parts[1], parts[2])
    print_output.gg_print(parts, result)


try:
    main(sys.argv)
except ValueError as error:
    print(error)
except SyntaxError as error:
    print(error)
