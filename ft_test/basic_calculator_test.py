from src.computor import Computor

NOK_LINE = '\033[91m'
END_LINE = '\033[0m'
OK_LINE = '\033[92m'


def execute_test(test):
    print(test[0], end=' - ')
    result = Computor().compute(test[0])
    if result == test[1]:
        print(OK_LINE + 'OK' + END_LINE)
    else:
        print(NOK_LINE + 'NOK' + END_LINE)
        print(result, test[1])


def tests():
    print('\n *** basic tests ***')
    add_test = [
        ['1 + 1', 2],
        ['1 + (-1)', 0],
        ['1 + 2', 3],
        ['3 + 1', 4],
        ['2 + 126757667576', 126757667578],
        ['1 - 1', 0],
        ['1 - 2', -1],
        ['1 - 23567235273527', -23567235273526],
        ['-1 + 1', 0],
        ['-2 + 1', -1],
        ['-1 + 1 + 1', 1],
        ['-2 + 1 + 256', 255],
        ['1 + 1 - 3 + 1 + 2 - 3', -1],
    ]

    mult_test = [
        ['1 / 1', 1],
        ['1 / 2', 0.5],
        ['1 * 1', 1],
        ['1 * 2', 2],
        ['1 * (-1)', -1],
        ['1 / (-1)', -1],
        ['1 / (-2)', -0.5],
        ['1 * (-2)', -2],
        ['2 * 0.5', 1],
        ['2 * 0.6', 1.2],
        ['0.5 * 0.6', 0.3],
        ['0.5 / 2', 0.25],
        ['1 / 3', 0.33333333],
        ['0.3333333333333333 * 3', 1],
        ['1 * 1 / 1 * 1 / (-1) * (-1)', 1],
        ['2 * 2 / 2 * 1 / (-2) * (-1)', 1],
        ['1 * 2 / 4 * 2 / (-2) * 1', -0.5],
    ]

    add_mult_test = [
        ['1 - 1 / 1 * 1 + 1', 1],
        ['2 - 1 / 1 * 2 + 0', 0],
        ['1 - 1 / 2 * 3 + 0.5 * 2', 0.5],
        ['1 - 1 / 2 * 3 + 0.5 * 2 - 1 / 2', 0],
        ['2 * 0.5 - 1 / 2 * 3 + 0.5 * 2 - 1 / 2', 0],
    ]

    parenthese_test = [
        ['(2)', 2],
        ['2 * (2)', 4],
        ['2 * ( 2 )', 4],
        ['2 * (-2)', -4],
        ['(2 * (2))', 4],
        ['2 * (2 + 2)', 8],
        ['2 * (2 - 2)', 0],
        ['2 * ((((2 + 2)) + 1))', 10],
        ['2 * (2 - 2)', 0],
        ['2 * (2 * 3)', 12],
        ['((2 * 2) + 2) * 3', 18]
    ]

    for test in add_test:
        execute_test(test)

    for test in mult_test:
        execute_test(test)

    for test in add_mult_test:
        execute_test(test)

    for test in parenthese_test:
        execute_test(test)


tests()
