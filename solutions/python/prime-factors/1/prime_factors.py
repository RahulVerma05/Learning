def factors(value):
    f_list = []
    remain = value
    if value == 1:
        return f_list
    i = 2
    while i <= remain:
        while remain%i == 0:
            f_list.append(i)
            remain = remain/i
        i += 1
    if remain > 1:
        f_list.append(remain)
    return f_list
