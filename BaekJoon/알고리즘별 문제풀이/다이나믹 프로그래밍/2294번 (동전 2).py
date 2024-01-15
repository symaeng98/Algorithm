INF = 1e9
n, k = map(int, input().split())
coins = list(set([int(input()) for _ in range(n)]))
coins.sort()
dp = [INF]*100001

for coin in coins:
    dp[coin] = 1

for i in range(1, k+1):
    for coin in coins:
        if coin >= i:
            break
        dp[i] = min(dp[i], dp[i-coin] + dp[coin])

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])