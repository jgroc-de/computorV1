from src.is_ import is_number
from .token import Token
from .providers import number, variable, operator, openingSeparator, closingSeparator


class Lexer:
    def tokenize(self, calculus: str) -> list:
        tokens = []
        calculus = calculus.replace('X', '1*X')
        count = len(calculus)
        try:
            i = 0
            while i < count:
                current_character = calculus[i]
                i += 1
                found = False
                for provider in self.providers:
                    if provider.isMyResponsability(current_character):
                        [token, i] = provider.getToken(
                            current_character, calculus, i)
                        found = True
                        break
                if not found:
                    raise ValueError(
                        '\n' + calculus + '\n' + (' ' * (i - 1)) + '^: lexer error here -> invalid characters')
                tokens.append(token)
            return tokens
        except ValueError as error:
            print(error)
            return []

    def __init__(self):
        self.providers = [
            number.Number(),
            variable.Variable(),
            openingSeparator.OpeningSeparator(),
            closingSeparator.ClosingSeparator(),
            operator.Operator(),
        ]
