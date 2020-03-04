def print_solution(result: float):
    if len(result) == 0:
        raise ValueError('delta is < 0, no solutions')
    elif len(result) == 1:
        text = 'x = {}'
        print(text.format(result[0]))
    else:
        text1 = 'x1 = {}'
        text2 = 'x2 = {}'
        print(text1.format(result[0]))
        print(text2.format(result[1]))


def print_degree(tab):
    max = 0
    for i in range(0, 3):
        if tab[i] != 0:
            max = i
    print('Polynomial degree: ' + str(max))


def print_reduced_form(tab):
    reduced_form = ''
    print(tab)
    j = 0
    for i in tab:
        if i != 0:
            if len(reduced_form):
                if i > 0:
                    reduced_form += ' + '
                else:
                    reduced_form += ' - '
            reduced_form += str(i)
            if j == 1:
                reduced_form += ' * X'
            elif j == 2:
                reduced_form += ' * X^2'
        j += 1

    text = 'Reduced form: {} = 0'
    print(text.format(reduced_form))


def gg_print(members_by_degree: dict, result: float):
    print_reduced_form(members_by_degree)
    print_degree(members_by_degree)
    print_solution(result)
