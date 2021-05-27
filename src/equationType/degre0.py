from .degreX import DegreX


class Degre0(DegreX):
    all = True

    def __init__(self, equation: list):
        DegreX.__init__(self, equation)
        if len(equation) != 1:
            raise ValueError('too much params for degre 0')

    def solve(self):
        if self.equation[0] == 0:
            self.all = True
        else:
            self.all = False

    def to_string(self):
        if self.all:
            return "Any value for X will work"
        else:
            return "No solution"
