def check_separators(separators: list):
    result = 0
    for separator in separators:
        if separator.lexeme == '(':
            result += 1
        else:
            result -=1
        if result < 0:
            raise(ValueError('incorrect closing parentheses!'))
    if result != 0:
        raise(ValueError('incorrect opening parentheses!'))
        

def check_validity(tokens: list) -> bool:
    error = 'incorrect format, element {} can\'t be at this place'
    save = 'operator'
    separators = []
    for token in tokens:
        if token.l_type == 'separator':
            if (token.lexeme == '(' and save != 'operator') or (token.lexeme == ')' and save not in ['variable', 'number']):
                raise(ValueError(error.format(token.lexeme)))
            separators.append(token)
            continue
        if token.l_type == save:
            raise(ValueError(error.format(token.lexeme)))
        elif token.l_type in ['number', 'variable'] and save != 'operator':
            raise(ValueError(error.format(token.lexeme)))
        save = token.l_type
    try:
        check_separators(separators)
        return True
    except ValueError as error:
        print(error)
        return False