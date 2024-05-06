n, k = map(int, input().split())
dp = [[0]*201 for _ in range(201)]
for i in range(n+1):
    dp[i][1] = 1
    dp[i][2] = i+1

for l in range(3, k+1):
    for i in range(n+1):
        tmp = 0
        for j in range(i+1):
            tmp += dp[j][l-1]
        dp[i][l] = tmp

print(dp[n][k]%1000000000)