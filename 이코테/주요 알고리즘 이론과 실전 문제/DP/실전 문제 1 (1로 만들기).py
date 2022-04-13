dp = [0] * 30001

N = int(input())

for i in range(2,N+1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i // 3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i],dp[i // 5] + 1)

print(dp[N])

# 1. 바로 이전 시행(1 작은 값)+1, 2. 각 수로 나누어 떨어진다면 그 나누어 떨어진 수의 결과값
# 1번과 2번 값 중 작은 값이 최솟값이기 때문에 min(dp[i-1]+1, dp[i//2]+1, ~~) 이어야 한다.
# 그러므로 if~elif가 아니라 모두 if여야 한다.