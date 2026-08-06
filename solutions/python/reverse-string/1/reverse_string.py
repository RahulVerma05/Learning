def reverse(text):
    rev = []
    for chr in text[::-1]:
        rev.append(chr)
    return "".join(rev)
