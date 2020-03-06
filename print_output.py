def print_solution(result: float):
    if len(result) == 0:
        raise ValueError('delta is < 0, no solutions')
    elif len(result) == 1:
        text = 'x = {}'
        print(text.format(round(result[0], 6)))
    else:
        text1 = 'x1 = {}'
        text2 = 'x2 = {}'
        print(text1.format(round(result[0], 6)))
        print(text2.format(round(result[1], 6)))


def get_degree(tab) -> int:
    max = 0
    for i in range(0, 3):
        if tab[i] != 0:
            max = i
    return max


def get_reduced_form(tab) -> str:
    reduced_form = ''
    j = 0
    for i in tab:
        if i != 0:
            i = round(i, 6)
            if len(reduced_form):
                if i > 0:
                    reduced_form += ' + ' + str(i)
                else:
                    reduced_form += str(i).replace('-', ' - ')
            else:
                reduced_form += str(i)
            if j == 1:
                reduced_form += ' * X'
            elif j == 2:
                reduced_form += ' * X^2'
        j += 1

    return 'Reduced form: {} = 0'.format(reduced_form)


def gg_print(members_by_degree: dict, result: float):
    print(get_reduced_form(members_by_degree))
    print('Polynomial degree: ' + str(get_degree(members_by_degree)))
    print_solution(result)
