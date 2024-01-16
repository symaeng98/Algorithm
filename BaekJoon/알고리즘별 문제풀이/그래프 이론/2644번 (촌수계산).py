from collections import deque

INF = 1e9
n = int(input())
v1, v2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
visited = [False]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(s):
    q = deque()
    distance[s] = 0
    q.append((0, s))
    while q:
        dist, v = q.popleft()
        visited[v] = True
        for g in graph[v]:
            if not visited[g]:
                distance[g] = min(distance[g], dist+1)
                q.append((dist+1, g))


bfs(v1)
if distance[v2] == INF:
    print(-1)
else:
    print(distance[v2])