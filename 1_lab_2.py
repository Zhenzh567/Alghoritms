def calculate(s):
    s = s.replace(' ', '')

    if not is_valid(s):
        raise ValueError("Неправильные скобки")

    while '(' in s:
        c = s.index(')')
        o = s.rindex('(', 0, c)
        inner = s[o+1:c]
        if o > 0 and s[o-1] == '-':
            result = -calc(inner)
            s = s[:o-1] + str(result) + s[c+1:]
        else:
            result = calc(inner)
            s = s[:o] + str(result) + s[c+1:]

    return calc(s)


def calc(s):
    nums = []
    ops = []
    i = 0
    while i < len(s):
        if s[i].isdigit() or s[i] == '.':
            num = ''
            while i < len(s) and (s[i].isdigit() or s[i] == '.'):
                num += s[i]
                i += 1
            nums.append(float(num))
            continue

        if s[i] == '-' and (i == 0 or s[i-1] in '+-*/'):
            num = '-'
            i += 1
            while i < len(s) and (s[i].isdigit() or s[i] == '.'):
                num += s[i]
                i += 1
            nums.append(float(num))
            continue

        while ops and ops[-1] in '*/' and s[i] in '+-':
            apply(nums, ops)
        ops.append(s[i])
        i += 1

    while ops:
        apply(nums, ops)

    return nums[0]


def apply(nums, ops):
    b = nums.pop()
    a = nums.pop()
    op = ops.pop()
    if op == '+': nums.append(a + b)
    elif op == '-': nums.append(a - b)
    elif op == '*': nums.append(a * b)
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Деление на ноль")
        nums.append(a / b)


def is_valid(text):
    brackets = ''.join(ch for ch in text if ch in '()')
    while '()' in brackets:
        brackets = brackets.replace('()', '')
    return not brackets

