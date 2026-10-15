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


def calc(s):
    if not s.endswith("="):
        raise ValueError("Нужен '=' в конце")
    s = s[:-1].replace(" ", "")

    if s == "":
        raise ValueError("Пустое выражение")

    if not is_valid(s):
        raise ValueError("Неправильные скобки")

    pr = {"+": 1, "-": 1, "*": 2, "/": 2}
    out = []
    ops = []

    i = 0
    while i < len(s):
        ch = s[i]

        if ch.isdigit() or ch == ".":
            num = ""
            while i < len(s) and (s[i].isdigit() or s[i] == "."):
                num += s[i]
                i += 1
            out.append(float(num))
            continue

        if ch == "-" and (i == 0 or s[i - 1] in "+-*/("):
            if i + 1 < len(s) and s[i + 1] == "(":
                out.append(0.0)
                ops.append("-")
                i += 1
                continue
            num = "-"
            i += 1
            while i < len(s) and (s[i].isdigit() or s[i] == "."):
                num += s[i]
                i += 1
            out.append(float(num))
            continue

        if ch == "(":
            ops.append(ch)
        elif ch == ")":
            while ops and ops[-1] != "(":
                out.append(ops.pop())
            if ops:
                ops.pop()
        else:
            while ops and ops[-1] != "(" and pr.get(ops[-1], 0) >= pr[ch]:
                out.append(ops.pop())
            ops.append(ch)

        i += 1

    while ops:
        out.append(ops.pop())

    st = []
    for t in out:
        if isinstance(t, str) and t in "+-*/":
            if len(st) < 2:
                raise ValueError("Неправильное выражение")
            b = st.pop()
            a = st.pop()
            if t == "+":
                st.append(a + b)
            elif t == "-":
                st.append(a - b)
            elif t == "*":
                st.append(a * b)
            elif t == "/":
                if b == 0:
                    raise ZeroDivisionError("Деление на ноль")
                st.append(a / b)
        else:
            st.append(t)

    if len(st) != 1:
        raise ValueError("Неправильное выражение")

    return st[0]


print(calc("(2+3)*4="))
print(calc("10/(2+3)="))
print(calc("2+3*4="))
print(calc("2--3="))
print(calc("1-(-(2+3))="))
print(calc("-(2+3)*4="))
print(calc("((2+3))="))
print(calc("-2*(4+4)-5="))
