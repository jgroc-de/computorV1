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
    if sign == '-':
        number = -number

    return [power, number]



def parse_members(equation: str) -> list:
    equation_parts = re.split('([+-])', equation)
    sign = ['+']
    [sign.append(equation_parts[i]) for i in range(0, len(equation_parts)) if equation_parts[i] in ['+', '-']]
    equation_parts = [item for item in equation_parts if item and item not in ['+', '-']]
    if len(sign) > len(equation_parts):
        sign.remove(0)
    equation_parts = [item.split('*') for item in equation_parts]
    members_by_degree = {0: [0], 1: [0], 2: [0]}
    for part in equation_parts:
        tosign = sign.pop()
        tmp = get_power_and_coef(part, tosign)
        if tmp[1] > 2 or tmp[1] < 0:
            raise ValueError('I can\'t manage power > 2 or < 0')
        members_by_degree[tmp[0]].append(tmp[1])

    return [sum(item) for item in members_by_degree]


def build_equation(equation: str) -> list:
    throw_exception_if_not_valid(equation)
    equation_parts = equation.split('=')
    is_empty(equation_parts[0])
    is_empty(equation_parts[1])
    #manque single variable
    leftPart = parse_members(equation_parts[0])
    rightPart = parse_members(equation_parts[1])

    return [leftPart[i] - rightPart[i] for i in range(0, 2)]