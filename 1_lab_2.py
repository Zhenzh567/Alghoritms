def is_valid(text):
    if text == "":
        return False
    
    stack = []
    for ch in text:
        if ch == "(":
            stack.append(ch)
        if ch == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False


def calculate(s):
    s = s.replace(" ", "")
    
    if not is_valid(s):
        raise ValueError("Неправильные скобки")
    
    pos = [0]
    
    def read_number():
        start = pos[0]
        
        for i in range(pos[0], len(s)):
            ch = s[i]
            if ch.isdigit() or ch == ".":
                pos[0] += 1
            else:
                break
        
        return float(s[start:pos[0]])
    
    def read_factor():
        ch = s[pos[0]]
        
        if ch == "-":
            pos[0] += 1
            value = read_factor()
            return -value
        
        if ch == "(":
            pos[0] += 1
            value = read_expression()
            pos[0] += 1
            return value
        
        return read_number()
    
    def read_term():
        result = read_factor()
        
        for i in range(pos[0], len(s)):
            if pos[0] >= len(s):
                break
            
            ch = s[pos[0]]
            
            if ch == "*" or ch == "/":
                pos[0] += 1
                value = read_factor()
                
                if ch == "*":
                    result = result * value
                else:
                    if value == 0:
                        raise ZeroDivisionError("Деление на ноль")
                    result = result / value
            else:
                break
        
        return result
    
    def read_expression():
        result = read_term()
        
        for i in range(pos[0], len(s)):
            if pos[0] >= len(s):
                break
            
            ch = s[pos[0]]
            
            if ch == "+" or ch == "-":
                pos[0] += 1
                value = read_term()
                
                if ch == "+":
                    result = result + value
                else:
                    result = result - value
            else:
                break
        
        return result
    
    result = read_expression()
    
    if pos[0] != len(s):
        raise ValueError("Лишние символы")
    
    return result


print(calculate("(2+3)*4"))
print(calculate("10/(2+3)"))
print(calculate("(1+2)*(3-4)"))
print(calculate("2+3*4"))
print(calculate("1-(-(2+3))"))
print(calculate("-(2+3)*4"))
print(calculate("2--3"))

