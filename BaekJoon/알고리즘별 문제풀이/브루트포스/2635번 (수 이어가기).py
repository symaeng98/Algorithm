n = int(input())
result = []
for k in range(1, n+1):
    first = n
    second = k
    tmp = [n, k]

    while True:
        next = first - second
        if next >= 0:
            tmp.append(next)
            first = second
            second = next
        else:
            if len(tmp) > len(result):
                result = tmp
            break

print(len(result))
for r in result:
    print(r, end=" ")