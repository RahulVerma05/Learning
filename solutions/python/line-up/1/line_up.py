def line_up(name, number):
    number = str(number)
    if len(number) == 1:
        if number[-1] == '1':
            return f'{name}, you are the {number}st customer we serve today. Thank you!'
        elif number[-1] == '2':
            return f'{name}, you are the {number}nd customer we serve today. Thank you!'
        elif number[-1] == '3':
            return f'{name}, you are the {number}rd customer we serve today. Thank you!'
        else:
            return f'{name}, you are the {number}th customer we serve today. Thank you!'

    else:
        if number[-1] == '1':
            if number[-2] != '1':
                return f'{name}, you are the {number}st customer we serve today. Thank you!'
        elif number[-1] == '2':
            if number[-2] != '1':
                return f'{name}, you are the {number}nd customer we serve today. Thank you!'
        elif number[-1] == '3':
            if number[-2] != '1':
                return f'{name}, you are the {number}rd customer we serve today. Thank you!'
        return f'{name}, you are the {number}th customer we serve today. Thank you!'
