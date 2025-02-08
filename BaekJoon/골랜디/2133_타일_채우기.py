n = int(input())
dp = [0]*31
dp[2] = 3
dp[4] = 11
for i in range(6, n+1):
    if i % 2 != 0:
        continue
    now = i
    dp[i] += dp[now-2]*dp[2]
    now -= 2

    while now >= 2:
        dp[i] += dp[now-2]*2
        now -= 2

    dp[i] += 2

# print(dp)
print(dp[n])
