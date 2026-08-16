def square_root(number):
    num = number//2
    if number == 1:
        return 1
    for i in range(2,num+1):
        square = i**2
        if square == number:
            return i
        
            
