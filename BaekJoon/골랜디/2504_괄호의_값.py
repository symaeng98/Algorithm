t = list(input())
tmp = []

result = 0
now = 1
for i, s in enumerate(t):
    if s == "(":
        now *= 2
        tmp.append(s)
    elif s == "[":
        now *= 3
        tmp.append(s)
    elif s == ")":
        if not tmp or tmp[-1] == "[":
            result = 0
            break
        if t[i-1] == "(":
            result += now
        tmp.pop()
        now //= 2
    elif s == "]":
        if not tmp or tmp[-1] == "(":
            result = 0
            break
        if t[i-1] == "[":
            result += now
        tmp.pop()
        now //= 3

print(result)
