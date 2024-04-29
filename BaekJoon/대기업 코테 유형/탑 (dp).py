n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 100000001)

# 10   6   9   5   7   4
# 0    0   0   2

dp = [0]*(n+1)
for i in range(1, n+1):
    if arr[i-1] >= arr[i]:
        dp[i] = i-1
    else:
        index = dp[i-1]
        while True:
            if arr[index] >= arr[i]:
                dp[i] = index
                break
            index = dp[index]

for i in range(1, n+1):
    print(dp[i], end=" ")