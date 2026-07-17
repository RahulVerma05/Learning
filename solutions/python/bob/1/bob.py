def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob == "":
        return "Fine. Be that way!"
    is_question = hey_bob[-1] == '?'
    is_shouting = hey_bob == hey_bob.upper() and hey_bob != hey_bob.lower()
    if is_question and is_shouting:
        return "Calm down, I know what I'm doing!"
    if is_question:
        return 'Sure.'
    if is_shouting:
        return "Whoa, chill out!"
    
    
    return "Whatever."
