from collections import deque

n, k = map(int, input().split())
q = deque()
q.append(n)
dp = [-1 for _ in range(100001)]
dp[n] = 0

while q:
    s = q.popleft()
    if s == k:
        print(dp[s])
        break
    if 0 <= s-1 < 100001 and dp[s-1] == -1:
        dp[s-1] = dp[s] + 1
        q.append(s-1)
    if 0 < s*2 < 100001 and dp[s*2] == -1:
        dp[s*2] = dp[s]
        q.appendleft(s*2)
    if 0 <= s+1 < 100001 and dp[s+1] == -1:
        dp[s+1] = dp[s] + 1
        q.append(s+1)