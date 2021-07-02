from src.solution.solutionInterface import SolutionInterface


class EquationSolution(SolutionInterface):
    def __init__(self, result: tuple):
        self.__result = result
    
    def getResult(self):
        return self.__result
    
    def getResultForHumans(self):
        pass
    
    def __str__(self) -> str:
        return "to do"