t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    book = [True]*(n+1)
    arr.sort(key=lambda x:x[1])
    print(arr)

    result = 0
    for s, e in arr:
        for i in range(s, e+1):
            if book[i]:
                result += 1
                book[i] = False
                break

    print(result)