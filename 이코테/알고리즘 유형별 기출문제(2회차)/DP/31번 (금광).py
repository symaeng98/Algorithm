t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    arr = [[] for _ in range(n)]
    for j in range(n):
        arr[j] = tmp[j*m:j*m+m]

    for j in range(1,m):
        for k in range(n):
            if k == 0:
                arr[k][j] += max(arr[k][j-1], arr[k+1][j-1])
            elif k == n-1:
                arr[k][j] += max(arr[k][j-1], arr[k-1][j-1])
            else:
                arr[k][j] += max(arr[k][j-1], arr[k-1][j-1], arr[k+1][j-1])

    result = 0
    for j in range(n):
        result = max(result, arr[j][m-1])

    print(result)