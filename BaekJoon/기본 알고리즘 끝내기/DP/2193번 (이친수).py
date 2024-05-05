n = int(input())
dp = [[1, 1] for _ in range(91)]
dp[1][0], dp[1][1] = 0, 1
dp[2][0], dp[2][1] = 1, 0
dp[3][0], dp[3][1] = 1, 1

for i in range(4, n+1):
    dp[i][0] = sum(dp[i-1])
    dp[i][1] = dp[i-1][0]
print(sum(dp[n]))