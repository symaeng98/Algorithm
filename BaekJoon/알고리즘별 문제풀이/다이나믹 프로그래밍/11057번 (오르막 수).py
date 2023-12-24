n = int(input())
dp = [[] for _ in range(n+1)]

if n == 1:
    print(10)
elif n == 2:
    print(55)
else:
    dp[1].append(10)
    for i in range(1, 11):
        dp[2].append(i)
    for i in range(3, n+1):
        for j in range(1, 11):
            dp[i].append(sum(dp[i-1][:j]))

    print(sum(dp[n])%10007)