n = int(input())
arr = list(map(int, input().split()))
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
now = max(dp)
result = []
for i in range(n-1, -1, -1):
    if dp[i] == now and (not result or result[-1] > arr[i]):
        now -= 1
        result.append(arr[i])

result.reverse()
print(*result)
# 6
# 10 20 10 30 20 50