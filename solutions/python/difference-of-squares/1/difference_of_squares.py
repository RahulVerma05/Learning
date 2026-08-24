def square_of_sum(number):
    total = 0
    for i in range(number+1):
        total += i
    return total**2


def sum_of_squares(number):
    total_2 = 0
    for x in range(number+1):
        total_2 += x**2
    return total_2

def difference_of_squares(number):
    if square_of_sum(number) > sum_of_squares(number):
        return square_of_sum(number) - sum_of_squares(number)
    else:
        return sum_of_squares(number) - square_of_sum(number)