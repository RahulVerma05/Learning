def is_paired(input_string):
    stack = []
    for char in input_string:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            opening = stack.pop()
            if char == ")" and opening != "(":
                return False
            if char == "}" and opening != "{":
                return False
            if char == "]" and opening != "[":
                return False

    return len(stack) == 0
        
        
