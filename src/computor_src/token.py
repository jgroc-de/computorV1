class Token:
    lexeme = ''
    l_type = ''
    __dict__ = [lexeme, l_type]

    def __init__(self, lexeme: str, l_type: str):
        self.lexeme = lexeme
        self.l_type = l_type
        self.__dict__ = [lexeme, l_type]
