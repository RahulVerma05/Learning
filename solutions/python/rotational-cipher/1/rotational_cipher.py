def rotate(text, key):
    result = []
    for char in text:
        if char.isupper():
            shifted = chr((ord(char)-ord("A")+key)%26 + ord("A"))
            result.append(shifted)
        elif char.islower():
            shifted_2 = chr((ord(char)-ord("a")+key)%26 + ord("a"))
            result.append(shifted_2)
        else:
            result.append(char)
    return "".join(result)
             
