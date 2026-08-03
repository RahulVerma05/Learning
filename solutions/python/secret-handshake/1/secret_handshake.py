def commands(binary_str):
    codes = {-1:'wink',
             -2: 'double blink',
             -3: 'close your eyes',
             -4: 'jump'}
    result = []
    for i in range(-1,-6,-1):
        if binary_str[i] == '1':
            if i == -5:
                result.reverse()
            else:
                result.append(codes[i])

    return result
        