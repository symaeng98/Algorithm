code = list(map(int, input()))
if code[0] == 0:
    print(0)
else:
    n = len(code)
    code.insert(0, 0)
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        x, y = code[i-1], code[i]
        if y != 0:
            dp[i] += dp[i-1]
        if 10 <= 10*x+y <= 26:
            dp[i] += dp[i-2]
    print(dp[n] % 1000000)
