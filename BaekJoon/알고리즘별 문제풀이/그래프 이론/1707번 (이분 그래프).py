from collections import deque

def bfs(s, group):
    q = deque()
    q.append(s)
    visited[s] = group
    while q:
        x = q.popleft()
        for v in graph[x]:
            if visited[v] == 0:
                q.append(v)
                visited[v] = -visited[x]
            else:
                if visited[v] == visited[x]:
                    return False
    return True

k = int(input())
for _ in range(k):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n+1):
        if visited[i] == 0:
            result = bfs(i, 1)
            if not result:
                break
    if result:
        print("YES")
    else:
        print("NO")