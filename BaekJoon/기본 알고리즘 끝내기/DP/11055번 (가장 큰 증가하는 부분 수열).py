import copy

n = int(input())
arr = list(map(int, input().split()))
dp = copy.deepcopy(arr)

for i in range(n):
    for j in range(i, -1, -1):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+arr[i])

print(max(dp))