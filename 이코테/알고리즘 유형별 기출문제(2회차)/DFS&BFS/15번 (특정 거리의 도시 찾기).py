from collections import deque
INF = 1e9

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(x):
    distance[x] = 0
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        dist = distance[x]
        for v in graph[x]:
            if dist+1 < distance[v]:
                distance[v] = dist+1
                q.append(v)

bfs(x)
flag = False
for i in range(n+1):
    if distance[i] == k:
        print(i)
        flag = True

if not flag:
    print(-1)