from src.calculus_type import basic, equation


calculus_types = [
    basic.Basic(),
    equation.Equation(),
]


class Computor:
    def __init__(self):
        self.variables = {'X': '2.0'}

    def main(self, equation):
        try:
            result = self.compute(equation)
            print(result)
        except ValueError as error:
            print(error)
        except SyntaxError as error:
            print(error)

    def compute(self, calculus: str) -> float:
        taken_in_charge = False
        result = 0
        for calculus_type in calculus_types:
            if calculus_type.can_compute_this(calculus):
                result = calculus_type.compute(calculus)
                taken_in_charge = True

        if not taken_in_charge:
            raise SyntaxError('cant compute this')

        #result = round(result, 8)
        # for case -0.0
        if (result == 0):
            return 0.0
        return result
