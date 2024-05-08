def x_to_y(x, y):
    result = []
    while x > 0:
        mod = x % y
        result.append(mod)
        mok = x // y
        x = mok
    result.reverse()
    return result


n, b = map(int, input().split())
answer = x_to_y(n, b)

for a in answer:
    if a >= 10:
        print(chr(a+55), end="")
    else:
        print(a, end="")