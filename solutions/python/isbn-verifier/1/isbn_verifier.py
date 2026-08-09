def is_valid(isbn):
    isbn = isbn.replace('-','')
    total = 0
    if len(isbn) != 10:
        return False
    for i, ch in enumerate(isbn):
        if ch == 'X':
            if i != 9:
                return False
            digit = 10
        elif ch.isdigit():
            digit = int(ch)
        else:
            return False
        total += digit*(10-i)
    return total%11 == 0
