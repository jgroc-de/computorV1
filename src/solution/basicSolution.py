from src.solution.solutionInterface import SolutionInterface


class BasicSolution(SolutionInterface):
    def __init__(self, result):
        self.__result = result
    
    def getResult(self):
        return self.__result
    
    def getResultForHumans(self):
        return round(self.__result, 6)

    def __str__(self) -> str:
        return str(self.getResultForHumans())