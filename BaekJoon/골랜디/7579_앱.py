n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
a.insert(0, 0)
c.insert(0, 0)

tmp = [x for x in range(sum(c)+1)]
dp = [[0]*(sum(c)+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(len(tmp)):
        k = c[i]
        w = a[i]
        if j < k:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-k]+w)

result = 1e9
for i in range(n+1):
    for j in range(len(tmp)):
        if dp[i][j] >= m:
            result = min(result, j)

print(result)

# 5 60
# 30 10 20 35 40
# 3 0 3 5 4