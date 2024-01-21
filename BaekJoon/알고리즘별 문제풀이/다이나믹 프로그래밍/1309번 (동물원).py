n = int(input())
dp = [[0, 0] for _ in range(n+2)]
dp[1][0] = 1
dp[1][1] = 1
dp[2][0] = dp[1][0] + 2*dp[1][1]
for i in range(2, n+2):
    dp[i][0] = (dp[i-1][0] + 2*(dp[i-1][1]))%9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][1])%9901

print(dp[n+1][0])