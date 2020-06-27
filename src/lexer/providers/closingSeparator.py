from .lTypeInterface import LTypeInterface
from ..token import Token

class ClosingSeparator(LTypeInterface):
    l_type = 'cSeparator'
    separators = [')']
    error = 'next parenthese not matching any opening parantheses'

    def isMyResponsability(self, char) -> bool:
        if char in self.separators:
            return True
        return False
    
    def getToken(self, char, calculus, i) -> [Token, int]:
        return [Token(char, self.l_type, self.error), i]
