def is_armstrong_number(number):
    break_num = [int(num) for num in str(number)]
    sum = 0
    power = len(break_num)
    for i in break_num:
        sum += i**power
    return sum == number
    