from src.computor_src.lexer import Token
from src.ft_math import ft_pow, ft_sqrt


def get_next_token(tokens: list) -> str:
    token = tokens[0]
    del(tokens[0])

    return token.lexeme


def parenthese_step(tokens: list) -> float:
    lexeme = get_next_token(tokens)
    if lexeme == '(':
        result = parse_recursive(tokens)
        get_next_token(tokens)  # pour passer la parenthese fermante
        return result
    return float(lexeme)


def function_step(tokens: list) -> float:
    a = parenthese_step(tokens)
    if len(tokens) and tokens[0].lexeme in ['^', 'sqrt']:
        op = get_next_token(tokens)
        b = function_step(tokens)
        if op == '^':
            a = ft_pow(a, b)
        else:
            a *= ft_sqrt(b)

    return a

def mult_step(tokens: list) -> float:
    a = function_step(tokens)
    while len(tokens) and tokens[0].lexeme in ['/', '*']:
        op = get_next_token(tokens)
        b = function_step(tokens)
        if op == '*':
            a *= b
        elif op == '/':
            if b == 0:
                raise(ValueError('division by 0 is forbidden'))
            a /= b

    return a


def addition_step(tokens: list) -> float:
    a = mult_step(tokens)
    while len(tokens) and tokens[0].lexeme in ['-', '+']:
        op = get_next_token(tokens)
        b = mult_step(tokens)
        if op == '-':
            a -= b
        else:
            a += b

    return a


def parse_recursive(tokens: list) -> float:
    result = addition_step(tokens)

    return result
