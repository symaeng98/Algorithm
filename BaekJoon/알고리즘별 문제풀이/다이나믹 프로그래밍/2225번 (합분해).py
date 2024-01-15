n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]

if k == 1:
    print(1)
elif k == 2:
    print(n+1)
else:
    for i in range(n+1):
        dp[i][1] = 1
        dp[i][2] = i+1

    for i in range(3, k+1):
        for j in range(n+1):
            for l in range(0, j+1):
                dp[j][i] += dp[l][i-1]

    print(dp[n][k]%1000000000)
