def egg_count(display_value):
    binary = []
    number = display_value
    while number > 0:
        binary.append(number%2)
        number = number//2
    return binary.count(1)
    
        
