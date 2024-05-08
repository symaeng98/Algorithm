def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b

t = int(input())
for _ in range(t):
    result = 0
    arr = list(map(int, input().split()))
    for i in range(1, len(arr)):
        for j in range(i+1, len(arr)):
            print(i, j, gcd(arr[i], arr[j]))
            result += gcd(arr[i], arr[j])

    print(result)