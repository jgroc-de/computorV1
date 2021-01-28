from src.lexer.token import Token
from src.lexer.providers.variable import Variable
from src.ft_math import ft_pow, ft_sqrt
from src.is_ import is_float
from src.parser.steps import addition, stepAbstract


class Parser:
    X = 0

    def __init__(self):
        self.__init()
        self.X = 1

    def __init(self):
        self.error = False
        self.used_tokens = []
        self.current_token = False
        self.step = addition.Addition()

    def set_error(self, error, tokens: [Token]):
        i = 0
        print('')
        for token in self.used_tokens:
            print(token.lexeme, end='')
            i += len(token.lexeme)
        i -= len(token.lexeme)
        for token in tokens:
            print(token.lexeme, end='')
        print('')
        print((' ' * (i)) + '^ parser error: {}'.format(error))
        self.error = True

    def __get_next_token(self, tokens: [Token]) -> str:
        token = tokens[0]
        self.used_tokens.append(token)
        self.current_token = token
        del(tokens[0])

        return token

    def __get_next_number(self, tokens):
        token = self.__get_next_token(tokens)
        lexeme = token.lexeme
        if token.lexeme == '(':
            result = self.parse_recursive(tokens, False)
            if len(tokens) == 0:
                self.set_error(token.error, tokens)
                return 0.0
            # pour passer la parenthese fermante
            next_token = self.__get_next_token(tokens)
            if next_token.lexeme != ')':
                self.set_error("lexeme {} is {}".format(
                    next_token.lexeme, token.error), tokens)
                return 0.0
            return result
        if token.l_type == Variable.l_type:
            lexeme = 1
        if not is_float(lexeme):
            self.set_error("lexeme {} is not a number".format(lexeme), tokens)
            lexeme = 0
        return float(lexeme)

    def __check_and_compute(self, tokens, step: stepAbstract.StepAbstract):
        if not step:
            return self.__get_next_number(tokens)
        next_step = step.get_next_step()
        if next_step:
            a = self.__check_and_compute(tokens, next_step)
        else:
            a = self.__get_next_number(tokens)
        while len(tokens) and step.is_my_responsability(tokens[0].lexeme):
            op = self.__get_next_token(tokens)
            b = self.__check_and_compute(tokens, next_step)
            try:
                a = step.compute(op.lexeme, a, b)
            except ValueError as error:
                self.set_error(error, tokens)

        return a

    def parse_recursive(self, tokens: [Token], first_call: bool) -> float:
        if first_call:
            self.__init()
        if len(tokens) > 1 and self.step.is_my_responsability(tokens[0].lexeme):
            tokens[1].lexeme = tokens[0].lexeme + tokens[1].lexeme
            del(tokens[0])
        result = self.__check_and_compute(tokens, self.step)
        if self.error:
            raise ValueError('parser error')

        return result

    def cut_variables_bloc(self, tokens: [Token]) -> list:
        result = [[]]
        power = 0
        tmp = []
        variable = False
        for token in tokens:
            if addition.Addition().is_my_responsability(token.lexeme):
                result = self.__append_to_array(result, power, tmp)
                tmp = [token]
                power = 0
                variable = False
                continue
            if token.l_type == Variable.l_type or variable == True:
                if token.l_type == 'number':
                    power = int(token.lexeme)
                    variable = False
                else:
                    power = 1
                    variable = True
            tmp.append(token)
        result = self.__append_to_array(result, power, tmp)
        return result

    def __append_to_array(self, tab: list, power: int, element) -> list:
        while len(tab) <= power:
            tab.append([])
        tab[power] += element
        return tab
