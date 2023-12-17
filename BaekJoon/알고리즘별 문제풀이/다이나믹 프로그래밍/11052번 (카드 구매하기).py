n = int(input())
p = list(map(int, input().split()))
p.insert(0,0)

dp = [0]*1001
dp[1] = p[1]

for i in range(2, n+1):
    max_value = -1
    dp[i] = p[i]
    for j in range((i//2)+1):
        if max_value < dp[j]+dp[i-j]:
            max_value = dp[j] + dp[i-j]
    dp[i] = max_value

print(dp[n])