from src.is_ import is_number
from src.computor_src.token import Token
from src.computor_src import validator

def get_number(number: str) -> Token:
    return Token(number, 'number')


def get_operator(operator: str) -> Token:
    return Token(operator, 'operator')


def get_variable(variable: str) -> Token:
    return Token(variable, 'variable')


def get_separator(separator: str) -> Token:
    return Token(separator, 'separator')


def tokenize(calculus: str) -> list:
    tokens = []
    last_type = 'operator'
    count = len(calculus)
    i = 0
    while i < count:
        char = calculus[i]
        i += 1
        if char == ' ':
            continue
        if is_number(char) or (char == '-' and is_number(calculus[i]) and last_type in ['operator', 'separator']):
            lexeme = char
            while i < count and is_number(calculus[i]):
                lexeme += calculus[i]
                i += 1
            token = get_number(lexeme)
        elif char in ['+', '-', '/', '*', '=', '^']:
            token = get_operator(char)
        elif char == 'X':
            token = get_variable(char)
        elif char in ['(', ')']:
            token = get_separator(char)
        tokens.append(token)
        last_type = token.l_type
    try:
        validator.check_validity(tokens)
    except ValueError as error:
        print(error)
        return []
        
    return tokens
