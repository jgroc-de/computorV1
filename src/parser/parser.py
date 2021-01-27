from src.lexer.token import Token
from src.ft_math import ft_pow, ft_sqrt
from src.is_ import is_float
from src.parser.steps import addition, stepAbstract

class Parser:
    def __init__(self):
        self.__init()


    def __init(self):
        self.error = False
        self.used_tokens = []
        self.current_token = False
        self.step = addition.Addition()


    def setError(self, error, tokens: [Token]):
        i = 0
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


    def __get_next_number(self, tokens) -> float:
        '''
        if len(tokens) == 0:
            self.setError("missing closing parentheses", tokens)
            return 0
        '''
        token = self.__get_next_token(tokens)
        lexeme = token.lexeme
        if token.lexeme == '(':
            result = self.parse_recursive(tokens, False)
            if len(tokens) == 0:
                self.setError(token.error, tokens)
                return 0.0
            next_token = self.__get_next_token(tokens)  # pour passer la parenthese fermante
            if next_token.lexeme != ')':
                self.setError("lexeme {} is {}".format(next_token.lexeme, token.error), tokens)
                return 0.0
            return result
        if not is_float(lexeme):
            self.setError("lexeme {} is not a number".format(lexeme), tokens)
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
                self.setError(error, tokens)
        
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
