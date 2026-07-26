def is_isogram(phrase):
    phrase = phrase.lower()
    import string
    clean_phrase = phrase.translate(str.maketrans('','',string.punctuation))
    clean_phrase = clean_phrase.replace(" ","")
    clean_set = set(clean_phrase)
    return len(clean_set) == len(clean_phrase)