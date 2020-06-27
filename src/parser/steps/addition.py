from .stepAbstract import StepAbstract
from src.lexer.token import Token
from .multiplication import Multiplication

class Addition(StepAbstract):
    match = ['+', '-']

    def __init__(self):
        self.next = Multiplication()

    def compute(self, operator, left_part, right_part) -> float:
        number = 0
        if operator == '-':
            return left_part - right_part
        elif operator == '+':
            number = left_part + right_part
        return number
