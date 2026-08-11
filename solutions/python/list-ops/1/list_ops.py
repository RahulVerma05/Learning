def append(list1, list2):
    list1 = list1 + list2
    return list1


def concat(lists):
    final = []
    for list_n in lists:
        final += list_n
    return final


def filter(function, list):
    result = []
    for item in list:
        if function is None:
            if item:
                result.append(item)
        elif function(item):
            result.append(item)
    return result

def length(list):
    total = 0
    for char in list:
        total +=1
    return total


def map(function, list):
    result =[]
    for item in list:
        result.append(function(item))
    return result


def foldl(function, list, initial):
    from functools import reduce
    return reduce(function,list,initial)

from functools import reduce

def foldr(function, list, initial):
    def flipped_func(accumulator, item):
        return function(accumulator, item)

    return reduce(flipped_func, reversed(list), initial)

def reverse(list):
    final = []
    for i in range(len(list)-1,-1,-1):
        final.append(list[i])
    return final
