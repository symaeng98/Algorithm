n = int(input())

arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int,input().split()))


for i in range(1, n):
    arr[i][0] += arr[i-1][0]
    for j in range(i-1):
        arr[i][j+1] = arr[i][j+1] + max(arr[i-1][j], arr[i-1][j+1])
    arr[i][i] += arr[i-1][i-1]

result = 0
for a in arr[-1]:
    result = max(result, a)

print(result)