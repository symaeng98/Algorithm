case = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    result = 0
    a = v//p
    b = v%p
    result += a*l
    if b <= l:
        result += b
    else:
        result += l
    print(f"Case {case}: {result}")
    case += 1