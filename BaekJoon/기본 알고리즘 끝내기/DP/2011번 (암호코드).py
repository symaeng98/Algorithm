n = input()
if n[0] == "0":
    print(0)
else:
    dp = [0]*5001
    dp[0] = 1
    dp[1] = 1
    for i in range(1, len(n)):
        if n[i] != "0":
            dp[i+1] += dp[i]
        if 10 <= int(n[i-1]+n[i]) <= 26:
            dp[i+1] += dp[i-1]

    print(dp[len(n)]%1000000)