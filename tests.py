import os

equation_errors = [
    ["", 1],
    ["lol",  1],
    ["lol = lol",  1],
    [" 3 * X + 2 * Y = 0",  1],
    [" 3 * X = 2 * Y",  1],
    ["3 * X = 2 * Y ^ 2",  1],
    [" 3 * X ^ 1 * X ^ 2 = 0",  1],
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
    ["1 + X - X ^ 2 = 0", 0], #nombre d\'or\?
    ["3 * X ^ 2 = 0",  0],
    ["-2 + 3 * X ^ 2 = 0",  0],
    ["-2 + 3 * X ^ 2 + 4 * X = 0",  0],
    ["-2 + 4 * X + 3 * X ^ 2 = 0",  0],
]

def execute_test(test):
    print('test: ' + test[0])
    out = os.system('python3 computorV1 "{}"'.format(test[0]))
    if out == test[1] * 256:
        print('\033[92m' + 'OK' + '\033[0m')
    else:
        print('\033[91m' + 'NOK' + '\033[0m')


for test in equation_errors:
    execute_test(test)

for test in equation_0:
    execute_test(test)

for test in equation_1:
    execute_test(test)

for test in equation_2:
    execute_test(test)