t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    height = list(map(int, input().split()))
    dp = [1] * n

    for i in range(len(height)):
        for j in range(i):
            if height[j] < height[i]:
                dp[i] = max(dp[i], dp[j]+1)

    print(f"#{test_case} {n - max(dp)}")