import re
from misc import throw_exception_if_not_valid, is_number, is_empty


def get_power_and_coef(equation_part: list, sign: str) -> dict:
    number = 1
    power = 0
    
    for item in equation_part:
        if is_number(item):
            number *= float(item)
        else:
            tmp = item.split('^')
            if len(tmp) > 1:
                power += int(tmp[1])
            else:
                power += 1
    if power > 2:
        raise ValueError(
            'The polynomial degree is stricly greater than 2, I can\'t solve.')
    elif power < 0:
        raise ValueError('Negative power is not allowed')
    if sign == '-':
        number = -number

    return [power, number]



def parse_members(equation: str) -> list:
    equation_parts = re.split('([+-])', equation)
    sign = ['+']
    to_remove = []
    for i in range(0, len(equation_parts) - 1):
        part = equation_parts[i]
        if part == '-' or part == '+':
            sign.append(part)
            to_remove.append(i)
    remove_count = len(to_remove)
    for i in range(0, remove_count):
        equation_parts.pop(to_remove.pop())
    if len(sign) > len(equation_parts):
        sign.remove(0)
    equation_parts = [item.split('*') for item in equation_parts]
    members_by_degree = {0: [0], 1: [0], 2: [0]}
    while True:
        if len(equation_parts) == 0:
            break
        part = equation_parts.pop()
        if part == ['']:
            break
        if len(sign):
            tosign = sign.pop()
        else:
            tosign = '+'
        tmp = get_power_and_coef(part, tosign)
        members_by_degree[tmp[0]].append(tmp[1])

    return [sum(members_by_degree[i]) for i in range(0, 3)]


def build_equation(equation: str) -> list:
    throw_exception_if_not_valid(equation)
    equation_parts = equation.split('=')
    is_empty(equation_parts[0])
    is_empty(equation_parts[1])
    #manque single variable
    leftPart = parse_members(equation_parts[0])
    rightPart = parse_members(equation_parts[1])
    
    return [leftPart[i] - rightPart[i] for i in range(0, 3)]