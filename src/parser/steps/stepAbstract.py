from src.lexer.token import Token

class StepAbstract(object):
    match = []

    def __init__(self):
        self.next = False

    def is_my_responsability(self, lexeme: str) -> bool:
        if lexeme in self.match:
            return True
        return False
    
    def get_next_step(self):
        return self.next

    def compute(self, operator, left_part, right_part) -> float:
        ''' Define how to compute '''
        pass
