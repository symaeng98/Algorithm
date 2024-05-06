import copy

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)
dp = copy.deepcopy(arr)

for i in range(2, n+1):
    for j in range(i):
        dp[i] = max(dp[i], dp[j]+dp[i-j])

print(dp[n])