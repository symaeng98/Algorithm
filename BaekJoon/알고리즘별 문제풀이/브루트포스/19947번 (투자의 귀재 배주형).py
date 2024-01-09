h, y = map(int, input().split())
dp = [h]*11
for i in range(1, 3):
    dp[i] = int(dp[i-1]*1.05)
for i in range(3, 5):
    dp[i] = int(max(dp[i-1]*1.05, dp[i-3]*1.2))
for i in range(5, 11):
    dp[i] = int(max(dp[i-1]*1.05, dp[i-3]*1.2, dp[i-5]*1.35))

print(dp[y])
