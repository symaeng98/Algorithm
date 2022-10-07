N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
dp[0] = arr[0]
dp[1] = max(arr[0],arr[1])
for i in range(2, N):
    dp[i] = max(dp[i-1], (dp[i-2]+arr[i]))


print(dp[N-1])


# DP의 원리를 잘 보여주는 문제다.
# 어렵지는 않았지만 dp[2]까지 설정해주려 했던 점, 출력을 max로 하려했던 점, dp[i]와 비교하려 했던 점은 반성하자