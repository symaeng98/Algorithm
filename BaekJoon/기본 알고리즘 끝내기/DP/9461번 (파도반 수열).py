t = int(input())
dp = [1]*101
dp[4] = 1+1
dp[5] = dp[4]
dp[6] = dp[3] + dp[5]
dp[7] = dp[2] + dp[6]
dp[8] = dp[1] + dp[7]
for i in range(9, 101):
    dp[i] = dp[i-5] + dp[i-1]

for _ in range(t):
    n = int(input())
    print(dp[n])