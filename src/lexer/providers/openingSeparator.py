from .lTypeInterface import LTypeInterface
from ..token import Token

class OpeningSeparator(LTypeInterface):
    l_type = 'oSeparator'
    separators = ['(']
    error = 'no matching cloing parentheses'

    def isMyResponsability(self, char) -> bool:
        if char in self.separators:
            return True
        return False
    
    def getToken(self, char, calculus, i) -> [Token, int]:
        return [Token(char, self.l_type, self.error), i]
