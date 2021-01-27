from .stepAbstract import StepAbstract
from src.lexer.token import Token
from src.ft_math import ft_pow, ft_sqrt

class Function(StepAbstract):
    match = ['^', 'V']

    def __init__(self):
        self.next = False  

    def compute(self, operator, left_part, right_part) -> float:
        if operator == '^':
            return ft_pow(left_part, right_part)
        else:
            return left_part * ft_sqrt(right_part)