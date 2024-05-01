n = int(input())
arr = list(int(input()) for _ in range(n))

dp = [1]*n
for i in range(n):
    for j in range(0,i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))