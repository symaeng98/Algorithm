t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    arr = [[] for _ in range(n)]
    for j in range(n):
        arr[j] = tmp[j*m:(j+1)*m]

    for j in range(1, m):
        for k in range(n):
            if k == 0:
                arr[k][j] = arr[k][j] + max(arr[k][j-1], arr[k+1][j-1])
            elif k == n-1:
                arr[k][j] = arr[k][j] + max(arr[k-1][j-1], arr[k][j-1])
            else:
                arr[k][j] = arr[k][j] + max(arr[k-1][j-1], arr[k][j-1], arr[k+1][j-1])
    result = 0
    for j in range(n):
        result = max(result, arr[j][m-1])

    print(result)







# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2