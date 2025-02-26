t = int(input())
for _ in range(t):
    n = int(input())
    arr = [input() for _ in range(n)]

    arr.sort()

    result = True
    for i in range(n-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            result = False
            break

    if result:
        print("YES")
    else:
        print("NO")
