from collections import deque

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    build_time = list(map(int, input().split()))
    build_time.insert(0, 0)
    in_degree = [0]*(n+1)
    result = [0] * (n+1)
    graph = [[] for _ in range(n+1)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_degree[y] += 1

    w = int(input())

    q = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)
            result[i] = build_time[i]

    while q:
        x = q.popleft()
        for v in graph[x]:
            in_degree[v] -= 1
            result[v] = max(result[v], result[x]+build_time[v])
            if in_degree[v] == 0:
                q.append(v)

    print(result[w])

# 2
# 4 4
# 10 1 100 10
# 1 2
# 1 3
# 2 4
# 3 4
# 4
# 8 8
# 10 20 1 5 8 7 1 43
# 1 2
# 1 3
# 2 4
# 2 5
# 3 6
# 5 7
# 6 7
# 7 8
# 7