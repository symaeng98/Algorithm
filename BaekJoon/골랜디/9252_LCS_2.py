s1 = list(input())
s2 = list(input())
n = len(s1)
m = len(s2)

dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])

result = []
x, y = n, m
while x != 0 and y != 0:
    if dp[x-1][y] == dp[x][y]:
        x -= 1
    elif dp[x][y-1] == dp[x][y]:
        y -= 1
    else:
        result.append(s1[x-1])
        x -= 1
        y -= 1

result.reverse()
print(''.join(result))

# ACAYKP
# CAPCAK