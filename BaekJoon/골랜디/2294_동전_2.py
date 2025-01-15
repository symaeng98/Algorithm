n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
INF = 1e9
dp = [INF]*(k+1)
dp[0] = 0

for x in range(1, k+1):
    for coin in coins:
        now = x - coin
        if now < 0:
            continue
        dp[x] = min(dp[x], dp[now]+1)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])


# 3 15
# 1
# 5
# 12