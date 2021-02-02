from src.is_ import is_number
from .token import Token
from .providers import number, variable, operator, openingSeparator, closingSeparator


class Lexer:
    def tokenize(self, calculus: str) -> list:
        tokens = []
        count = len(calculus)
        i = 0
        while i < count:
            token = 0
            current_character = calculus[i]
            i += 1
            if current_character == ' ':
                continue
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
            if token.l_type == variable.Variable.l_type and len(tokens) and tokens[-1].lexeme != '*':
                tokens.append(
                    Token('1', number.Number.l_type, number.Number.error))
                tokens.append(
                    Token('*', operator.Operator.l_type, operator.Operator.error))
            tokens.append(token)
        return tokens

    def __init__(self):
        self.providers = [
            number.Number(),
            variable.Variable(),
            openingSeparator.OpeningSeparator(),
            closingSeparator.ClosingSeparator(),
            operator.Operator(),
        ]
