n, d = map(int, input().split())
arr = []
for _ in range(n):
    s, e, c = map(int, input().split())
    if (e > d) or (e - s) < c:
        continue
    arr.append((s, e, c))

dp = [i for i in range(d+1)]

for i in range(1, d+1):
    dp[i] = min(dp[i], dp[i-1]+1)
    for s, e, c in arr:
        dp[e] = min(dp[e], dp[s]+c)

print(dp[d])

