from collections import deque

def bfs(graph, visited, s):
    q = deque()
    q.append(s)
    while q:
        x = q.popleft()
        visited[x] = True
        for g in graph[x]:
            if visited[g]:
                return True
            q.append(g)

    return False

t = int(input())
for _ in range(t):
    n = int(input())
    tmp = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        graph[i].append(tmp[i-1])

    visited = [False]*(n+1)
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            if bfs(graph, visited, i):
                cnt += 1

    print(cnt)