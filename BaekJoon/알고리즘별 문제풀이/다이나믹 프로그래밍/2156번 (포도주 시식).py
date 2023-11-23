import sys
input = sys.stdin.readline

n = int(input())
grapes = [0]*10000
for i in range(n):
    grapes[i] = int(input())

dp = [0] * 10000
dp[0] = grapes[0]
dp[1] = grapes[0] + grapes[1]
dp[2] = max(grapes[0] + grapes[1], grapes[0]+grapes[2], grapes[1] + grapes[2])
for i in range(3, n):
    dp[i] = max(grapes[i]+dp[i-2], grapes[i]+grapes[i-1]+dp[i-3], dp[i-1])

print(dp[n-1])