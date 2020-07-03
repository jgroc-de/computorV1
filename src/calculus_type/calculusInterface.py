from src.pattern.singletonMeta import SingletonMeta

class CalculusInterface(metaclass=SingletonMeta):
    def can_compute_this(self, calculus: str) -> bool:
        ''' Define if can compute this or not '''
        pass

    def compute(self, calculus: str, variables: list) -> float:
        ''' Compute the required calculus '''
        pass
