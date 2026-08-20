def find(search_list, value):
    left = 0
    right = len(search_list) -1
    while left <= right:
        mid = (left+right)//2
        guess = search_list[mid]
        if guess == value:
            return search_list.index(value)
        elif guess > value:
            right = mid -1
        else:
            left = mid +1
    raise ValueError("value not in array")
