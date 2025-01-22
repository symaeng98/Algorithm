from collections import deque

n, k = map(int, input().split())
INF = 1e9
dp = [INF]*100001

q = deque()
q.append(n)
dp[n] = 0
result = 0
while q:
    x = q.popleft()
    if x == k:
        result += 1

    for t in [x*2, x-1, x+1]:
        if 0 <= t < 100001 and dp[t] >= dp[x]+1:
            dp[t] = dp[x]+1
            q.append(t)

print(dp[k])
print(result)
