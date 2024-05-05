n = int(input())
arr = list(int(input()) for _ in range(n))
if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0]+arr[1])
else:
    dp = [0]*10001
    dp[0] = arr[0]
    dp[1] = arr[0]+arr[1]
    dp[2] = max(arr[0]+arr[1], arr[0]+arr[2], arr[1]+arr[2])
    for i in range(3, n):
        dp[i] = max(dp[i-2]+arr[i], arr[i-1]+arr[i]+dp[i-3], dp[i-1])
    print(dp[n-1])