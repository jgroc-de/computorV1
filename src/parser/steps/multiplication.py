from .stepAbstract import StepAbstract
from src.lexer.token import Token
from .function import Function

class Multiplication(StepAbstract):
    match = ['/', '*']

    def __init__(self):
        self.next = Function()

    def compute(self, operator, left_part, right_part) -> float:
        if operator == '*':
            return left_part * right_part
        elif operator == '/':
            if right_part == 0:
                raise(ValueError('dividing by 0 is forbidden'))
            return left_part / right_part
