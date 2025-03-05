n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
a.insert(0, 0)
c.insert(0, 0)
dp = [[0]*(sum(c)+1) for _ in range(n+1)]
result = sum(c)

for i in range(1, n+1):
    for j in range(sum(c)+1):
        if j < c[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c[i]]+a[i])

        if dp[i][j] >= m:
            result = min(result, j)

# print(dp)
if m != 0:
    print(result)
else:
    print(0)
# 5 60
# 30 10 20 35 40
# 3 0 3 5 4

# 5 60
# 30 10 20 40 60
# 3 0 3 4 5