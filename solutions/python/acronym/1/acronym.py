def abbreviate(words):
    short = []
    for i in range(0,len(words)):
        if i == 0:
            short.append(words[0])
        if words[i] == " " or words[i] == "-" or words[i] == "_":
            if words[i+1].isalpha():
                short.append(words[i+1].upper())
    
    return "".join(short)
