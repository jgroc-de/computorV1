from .calculusInterface import CalculusInterface
from .basic import Basic

class Equation(CalculusInterface):
    def __init__(self):
        self.basic = Basic()


    def can_compute_this(self, calculus: str) -> bool:
        if calculus.count('=') != 1:
            return False        
        return True


    def compute(self, calculus: str) -> float:
        calculus_parts = calculus.split('=')
        if len(calculus_parts[0]) == 0 or len(calculus_parts[1]) == 0:
            raise ValueError('one part of the equation is empty')
        degree_results = []
        degree_parts = self.__parse_part(part)
        for part2 in degree_parts:
            degree_results.append(self.basic.compute(part2))
        result = self.__solve(degree_results)

        return result
    
    def extract_part(self, part, sign):
        degree_results = []
        degree_parts = self.__parse_part(part)
        for part2 in degree_parts:
            degree_results.append(self.basic.compute(part2))


    def __parse_part(self, calculus: str) -> list:
        return []


    def __solve(self, equation: []) -> float:
        return 0
