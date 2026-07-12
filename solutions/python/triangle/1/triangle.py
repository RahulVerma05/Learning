def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a == 0:
        return False
    if a == b and b == c:
        return True
    return False

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b < c or b + c < a or c + a < b:
        return False
    if a == b or b == c or a == c :
        return True
    return False

def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a + b < c or b + c < a or c + a < b:
        return False
    if a == b or b== c or c == a:
        return False
    return True
