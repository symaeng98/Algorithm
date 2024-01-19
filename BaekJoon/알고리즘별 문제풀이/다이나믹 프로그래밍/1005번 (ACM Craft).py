from collections import deque

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    d.insert(0, 0)
    graph = [[] for _ in range(n+1)]
    in_degree = [0]*(n+1)
    dp = [0]*(n+1)

    for i in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1

    w = int(input())

    q = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)
            dp[i] = d[i]

    while q:
        x = q.popleft()

        for i in graph[x]:
            in_degree[i] -= 1
            dp[i] = max(dp[i], dp[x] + d[i])
            if in_degree[i] == 0:
                q.append(i)

    print(dp[w])