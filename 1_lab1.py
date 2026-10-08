def is_valid(text):
    if text == "":
        return False
    
    stack = []
    
    for char in text:
        if char in "([{":
            stack.append(char)
        
        elif char == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
        
        elif char == "]":
            if not stack or stack[-1] != "[":
                return False
            stack.pop()
        
        elif char == "}":
            if not stack or stack[-1] != "{":
                return False
            stack.pop()
    
    return not stack
