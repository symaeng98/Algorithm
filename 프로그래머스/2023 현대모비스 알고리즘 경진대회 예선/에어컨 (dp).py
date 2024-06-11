def solution(temperature, t1, t2, a, b, onboard):
    INF = 1e9
    n = len(onboard)
    temperature, t1, t2 = temperature+10, t1+10, t2+10
    dp = [[INF]*100 for _ in range(n)]
    dp[0][temperature] = 0
    for i in range(1, n):
        if onboard[i]:
            start = t1
            end = t2
        else:
            start = min(t1, temperature)
            end = max(t2, temperature)

        for j in range(start, end+1):
            if dp[i-1][j-1] != INF:
                if temperature < j:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1]+a)
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
            if dp[i-1][j] != INF:
                if temperature == j:
                    dp[i][j] = min(dp[i][j], dp[i-1][j])
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j]+b)
            if dp[i-1][j+1] != INF:
                if temperature > j:
                    dp[i][j] = min(dp[i][j], dp[i-1][j+1]+a)
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j+1])

    return min(dp[n-1])