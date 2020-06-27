class Token:
    def __init__(self, lexeme: str, l_type: str,  error: str):
        self.lexeme = lexeme
        self.l_type = l_type
        self.error = error
