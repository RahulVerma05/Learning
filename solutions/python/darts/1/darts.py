def score(x, y):
    while 25 < (x)**2 + (y)**2 <=100:
        return 1
    while 1 < (x)**2 + (y)**2 <=25:
        return 5
    while 0 <= (x)**2 + (y)**2 <=1:
        return 10
    while  (x)**2 + (y)**2 > 100:
        return 0