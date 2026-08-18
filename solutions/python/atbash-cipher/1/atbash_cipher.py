def encode(plain_text):
    cleaner = []
    for c in plain_text:
        if c.isalnum():
            cleaner.append(c.lower())
    
    encode_pl = []
    for char in cleaner:
        if 'a' <= char <= 'z':
            encode_pl.append(chr(ord('a')+ord('z')-ord(char)))
        else:
            encode_pl.append(char)
    result = "".join(encode_pl)
    return " ".join(result[i:i+5] for i in range(0, len(result), 5))


def decode(ciphered_text):
    cleaner = []
    for c in ciphered_text:
        if c.isalnum():
            cleaner.append(c.lower())
    
    decode_pl = []
    for char in cleaner:
        if 'a' <= char <= 'z':
            decode_pl.append(chr(ord('a')+ord('z')-ord(char)))
        else:
            decode_pl.append(char)
    return "".join(decode_pl)

