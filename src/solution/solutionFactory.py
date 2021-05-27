from src.solution.EquationSolution import EquationSolution
from src.solution.basicSolution import BasicSolution


class SolutionFactory:
    def getSolution(self, result):
        if type(result) == int or type(result) == float:
            return BasicSolution(result)
        return EquationSolution(result)