from src.is_ import is_number
from ..token import Token
from .lTypeInterface import LTypeInterface

class Number(LTypeInterface):
    l_type = 'number'
    other_type = ['operator', 'oSeparator', 'cSeparator']
    error = 'not a number'

    def __init__(self):
        pass

    def isMyResponsability(self, char) -> bool:
        if is_number(char):
            return True
        return False
    
    def getToken(self, char, calculus, i) -> [Token, int]:
        lexeme = char
        while i < len(calculus) and is_number(calculus[i]):
            lexeme += calculus[i]
            i += 1
        return [Token(lexeme, self.l_type, self.error), i]
