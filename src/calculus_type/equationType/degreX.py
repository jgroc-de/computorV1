class DegreX:
    equation = []

    def __init__(self, equation: list):
        self.degre = len(equation) - 1
        self.equation = equation

    def solve(self):
        ''' compute solution for the equation '''

    def __get_degree(self) -> str:
        return "Polynomial degree: " + str(self.degre) + "\n"

    def __get_reduced_equation(self) -> str:
        reduced_equation = ""
        power = 0
        for part in self.equation:
            if part != 0:
                part = round(part, 6)
                reduced_equation += self.__format_part(
                    len(reduced_equation), part, power)
            power += 1

        return "Reduced form: " + reduced_equation + " = 0\n"

    def __format_part(self, is_not_empty: int, part: int, power: int) -> str:
        reduced_part = ""
        if is_not_empty:
            if part > 0:
                reduced_part += ' + ' + str(part)
            else:
                reduced_part += str(part).replace('-', ' - ')
        else:
            reduced_part += str(part)
        if power == 1:
            reduced_part += ' * X'
        elif power > 1:
            reduced_part += ' * X^' + str(power)

        return reduced_part

    def to_string(self) -> str:
        return "The polynomial degree is stricly greater than 2, I can't solve"

    def __str__(self):
        return self.__get_reduced_equation() + self.__get_degree() + self.to_string()
