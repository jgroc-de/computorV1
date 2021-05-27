from .degre0 import Degre0
from .degre1 import Degre1
from .degre2 import Degre2
from .degreX import DegreX

class EquationSolverFactory:
    def getSolver(self, equation_parts: list) -> DegreX:
        if len(equation_parts) == 1:
            return Degre0(equation_parts)
        elif len(equation_parts) == 2:
            return Degre1(equation_parts)
        elif len(equation_parts) == 3:
            return Degre2(equation_parts)
        else:
            return DegreX(equation_parts)