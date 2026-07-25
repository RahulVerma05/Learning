def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    lower_sentance = set(sentence.lower())
    return alphabet <= lower_sentance
