t = int(input())
for _ in range(t):
    k = int(input())
    arr = list(map(int, input().split()))
    s_arr = [0]*(k+1)
    for i in range(1, k+1):
        s_arr[i] = arr[i-1]
        s_arr[i] += s_arr[i-1]

    dp = [[0]*(k+1) for _ in range(k+1)]

    for i in range(1, k+1):
        for j in range(i+1, k+1):
            start = j-i
            end = j

            min_value = 100000000
            for mid in range(start, end):
                min_value = min(min_value, dp[start][mid]+dp[mid+1][end])

            dp[start][end] = min_value + s_arr[end]-s_arr[start-1]

    print(dp[1][k])
