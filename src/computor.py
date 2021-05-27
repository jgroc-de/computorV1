from src.solution.solutionInterface import SolutionInterface
from src.calculus_type.CalculusTypeFactory import CalculusTypeFactory


class Computor:
    def __init__(self):
        #self.__variables = {'X': '2.0'}
        self.__calculsTypeFactory = CalculusTypeFactory()
        pass

    def computeAndPrint(self, calculus: str):
        result = 0
        try:
            result = self.compute(calculus)
            print(result)
        except ValueError as error:
            print(error)
        except SyntaxError as error:
            print(error)

    def compute(self, calculus: str) -> SolutionInterface:
        try:
            calculus_type = self.__calculsTypeFactory.getCalculusType(calculus)
            return calculus_type.compute(calculus)
        except SyntaxError as error:
            print(error)
