def sum_of_multiples(limit, multiples):
    elemnts = []
    total = 0
    
    for multipler in multiples:
        if multipler == 0:
            continue
        x = limit//multipler
        for i in range(1,x+1):
            y = multipler*i
            if y < limit:
                elemnts.append(y)
    elemnts = set(elemnts)
    for m in elemnts:
        total += m
    return total
