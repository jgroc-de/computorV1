from .lTypeInterface import LTypeInterface
from ..token import Token


class Variable(LTypeInterface):
    l_type = 'variable'
    variables = ['X', 'Y']
    error = 'not a variable'

    def isMyResponsability(self, char) -> bool:
        if char in self.variables:
            return True
        return False

    def getToken(self, char, calculus, i) -> [Token, int]:
        return [Token(char, self.l_type, self.error), i]
