n = int(input())
arr = list(map(int, input().split()))
dpl = [1]*n
dpr = [1]*n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dpl[i] = max(dpl[i], dpl[j]+1)

for i in range(n-1, -1, -1):
    for j in range(i, n):
        if arr[j] < arr[i]:
            dpr[i] = max(dpr[i], dpr[j]+1)

result = 0
for i in range(n):
    result = max(result, dpl[i]+dpr[i]-1)

print(result)
# 10
# 1 5 2 1 4 3 4 5 2 1