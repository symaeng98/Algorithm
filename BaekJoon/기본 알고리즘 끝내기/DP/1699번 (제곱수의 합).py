INF = 1e9
n = int(input())
dp = [INF]*100001
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, n+1):
    for j in range(1, 400):
        if j**2 == i:
            dp[i] = 1
        elif j**2 < i:
            dp[i] = min(dp[i], dp[j**2]+dp[i-j**2])
        else:
            break

print(dp[n])