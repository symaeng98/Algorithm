n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [0]*(k+1)
dp[0] = 1

for i in arr:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]
print(dp[k])