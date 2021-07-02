from src.computor import Computor

NOK_LINE = '\033[91m'
END_LINE = '\033[0m'
OK_LINE = '\033[92m'


def execute_test(test):
    print(test[0], end=' - ')
    result = Computor().compute(test[0])
    if result.getResult() == test[1]:
        print(OK_LINE + 'OK' + END_LINE)
    else:
        print(NOK_LINE + 'NOK' + END_LINE)
        print(result.getResult(), test[1])


def tests():
    print('\n *** Equation degre 0  tests ***')
    valid_test = [
        ['1=0', False],
        ['0=1', False],
        ['0=0', True],
        ['1.2=5/4', True],
        ['3.333 = 10/3', False],
        ['1-1=0', True],
        ['1.1 = 1.2', False],
        ['-834678 = 0 -834678', True],
    ]

    for test in valid_test:
        execute_test(test)


tests()
