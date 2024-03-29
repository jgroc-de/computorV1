from src.computor import Computor

NOK_LINE = '\033[91m'
END_LINE = '\033[0m'
OK_LINE = '\033[92m'


def assert_equal(test):
    print('                  ', end='\r')
    print(test[0], end='')
    out = Computor().compute(test[0])
    if out.getResultForHumans() == test[1]:
        print(' - ' + OK_LINE + 'OK' + END_LINE)
    else:
        print(" - result: " + str(out.getResultForHumans()) + " - " + str(test[1]), end='')
        print(NOK_LINE + ' NOK' + END_LINE, end='')
        print('')
        exit()


def assert_throw(test):
    print('                  ', end='\r')
    print(test[0], end='')
    try:
        Computor().compute(test[0])
    except ValueError as error:
        if test[1] == 'value':
            print(' - ' + OK_LINE + 'OK' + END_LINE, end='')
        else:
            print(error, end=' - ')
            print(NOK_LINE + 'NOK' + END_LINE)
        return
    except SyntaxError as error:
        if test[1] == 'value':
            print(' - ' + OK_LINE + 'OK' + END_LINE, end='')
        else:
            print(error, end=' - ')
            print(NOK_LINE + 'NOK' + END_LINE)
        return


def tests():
    print(' *** validity tests ***')
    basic_op = [
        ["1+1", 2],
        ["1.1+2.2", 3.3],
        ["0.3+0.3+0.3-0.9", 0],
        ["2*4", 8],
        ["2/4", 0.5],
        ["1/3", 0.333333],
        ["0+0", 0],
        ["0-0", 0],
        ["2 * 3", 6],
        ["2 * 3 * 2 - 2", 10],
        ["2 * 3 + 3 * 2 / 2", 9],
        ["(2+5) * 2", 14],
        ["(5) * (2)", 10],
        ["(3 + 2) * (2 + 3)", 25],
        ["(3 + 2) / (2 + 3)", 1],
        ["(3 + 2.0) / (2 + 3)", 1],
        ["(3.0) / (3.0 + 3)", 0.5],
        ["((3.0)) / (3.0 + 3)", 0.5],
        ["((3.0) / (3.0 + 3))", 0.5],
        ["(3.0 + (3 + 4)) / (3.0 + 2)", 2],

    ]
    equation_errors = [
        #["1.1.1+2.2", 'value'],
        ["1+-1", 'value'],
        ["1*-1", 'value'],
        ["", 'value'],
        ["lol",  'value'],
        ["lol = lol",  0],
        [" 3 * X + 2 * Y = 0",  0],
        [" 3 * X = 2 * Y",  0],
        ["3 * X = 2 * Y ^ 2",  0],
        [" 3 * X ^ 1 * X ^ 2 = 0",  0],
    ]

    equation_0 = [
        ["1 + 3 * X + 5 * X ^ 2 = 1 + 3 * X + 5 * X ^ 2",  0],
        ["1 = 0",  0],
        ["42 = 42",  0],
        ["42 = -42",  0],
        ["42 * X^0 = 42 * X^0",  0],
        ["42 * X^0 = 42 * X^0",  0],
        [" 42 * X^ 1 = 41 * X^1",  0],
        ["42 * X^2 = 42 * X^2", 0],
        ["42 * X^2 = 41 * X^2",  0],
        ["42 * X^3 = 42 * X^3",  0],
        ["42 * X^3 = 41 * X^3",  0],
    ]

    equation_1 = [
        ["X = 0",  0],
        ["X = 1",  0],
        ["X = -1",  0],
        ["9.3 * X  + 2 * X = 0",  0],
        ["X = 42 * 3",  0],
        ["3 * 5 * X = 42",  0],
        ["3 * 5 * X + 18 * X ^2 = 42 + 18 * X ^ 2",  0],
        ["3 * 5 * X + 18 * X ^ 2 - 18 * X ^ 2 = 42",  0],
        ["- 42 + 3 * 5 *X + 18 = 0",  0],
    ]

    equation_2 = [
        ["1 + X - X ^ 2 = 0", 0],  # nombre d\'or\?
        ["3 * X ^ 2 = 0",  0],
        ["-2 + 3 * X ^ 2 = 0",  0],
        ["-2 + 3 * X ^ 2 + 4 * X = 0",  0],
        ["-2 + 4 * X + 3 * X ^ 2 = 0",  0],
    ]

    for test in basic_op:
        assert_equal(test)

    for test in equation_errors:
        assert_throw(test)

    for test in equation_0:
        assert_equal(test)

    # for test in equation_1:
    #    assert_equal(test)

    # for test in equation_2:
    #    assert_equal(test)


tests()
