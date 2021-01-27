from .lTypeInterface import LTypeInterface
from ..token import Token

class Operator(LTypeInterface):
    l_type = 'operator'
    operator = ['+', '-', '/', '*', '=', '^']
    error = 'not an operator'

    def isMyResponsability(self, char) -> bool:
        if char in self.operator:
            return True
        return False
    
    def getToken(self, char, calculus, i) -> [Token, int]:
        return [Token(char, self.l_type, self.error), i]
