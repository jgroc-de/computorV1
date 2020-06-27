from .singletonMeta import SingletonMeta

class CalculusInterface(metaclass=SingletonMeta):
    def canComputeThis(self, calculus: str) -> bool:
        ''' Define if can compute this or not '''
        pass

    def compute(self, calculus: str) -> bool:
        ''' Compute the required calculus '''
        pass
