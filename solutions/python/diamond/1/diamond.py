def rows(letter):
    space = " "*(ord(letter)-ord("A"))
    i = ord("A")
    line = []
    while i <= ord(letter):
        if i == ord("A"):
            row = " " * (ord(letter) - i) + chr(i) + " " * (ord(letter) - i)
        else:
            row = " " * (ord(letter) - i) + chr(i) + " " * (2 * (i-ord("A")) - 1) + chr(i) + " " * (ord(letter) - i)
        i += 1
        line.append(row)
    if len(line) > 1:
        line += line[-2::-1]
    return line

