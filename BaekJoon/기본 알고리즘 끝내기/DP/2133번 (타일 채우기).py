n = int(input())
dp = [0]*31
dp[2] = 3
dp[4] = dp[2]*3 + 2
dp[6] = dp[4]*3 + dp[2]*2 + 2
for i in range(8, 31):
    if i % 2 != 0:
        dp[i] = 0
    else:
        dp[i] = dp[i-2]*3 + sum(dp[:i-3])*2 + 2

print(dp[n])