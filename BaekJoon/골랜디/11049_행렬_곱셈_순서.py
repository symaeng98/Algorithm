n = int(input())

INF = 2**31
dp = [[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][i] = 0

p = list(map(int, input().split()))
for _ in range(1, n):
    a, b = map(int, input().split())
    p.append(b)

for j in range(1, n+1):
    for i in range(j, 0, -1):
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+p[i-1]*p[k]*p[j])


print(dp[1][n])
# 3
# 5 3
# 3 2
# 2 6