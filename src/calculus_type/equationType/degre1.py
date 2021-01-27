from .degreX import DegreX


class Degre1(DegreX):
    solution = 0

    def __init__(self, equation: list):
        DegreX.__init__(self, equation)
        if len(equation) != 2:
            raise ValueError('too much params for degre 1')

    def solve(self):
        self.solution = - self.equation[0] / self.equation[1]

    def to_string(self) -> str:
        ccl = "The Solution is X = "
        if self.solution == 0:
            return ccl + "0"
        else:
            return ccl + str(self.solution) + " (or " + str(-self.equation[0]) + "/" + str(self.equation[1]) + ")"
