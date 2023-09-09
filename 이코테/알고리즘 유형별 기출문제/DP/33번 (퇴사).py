n = int(input())
arr = []

for i in range(1, n+1):
    t, p = map(int, input().split())
    arr.append((i,i+t-1,p))

sorted_arr = sorted(arr, key=lambda x:x[1])

dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = max(dp[:i+1])
    for s, e, p in sorted_arr:
        if e == i:
            dp[e] = max(dp[s-1] + p, dp[e])
print(max(dp))