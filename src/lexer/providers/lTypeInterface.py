from ..token import Token

class LTypeInterface:
    def isMyResponsability(self, char) -> bool:
        '''Define if it is the responsability of this provider'''
        pass
    
    def getToken(self, char, calculus, i) -> [Token, int]:
        '''generate Token'''
        pass