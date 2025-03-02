n = int(input())
arr = []
for _ in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))

dp = [1]*n
arr.sort()
for i in range(n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
# 8
# 1 8
# 3 9
# 2 2
# 4 1
# 6 4
# 10 10
# 9 7
# 7 6