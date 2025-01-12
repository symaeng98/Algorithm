import heapq

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())
INF = 1e9


def dijik(start, end):
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    while q:
        v, cost = heapq.heappop(q)
        for g in graph[v]:
            x, dist = g[0], g[1]
            if distance[x] < cost + dist:
                continue
            heapq.heappush(q, (x, cost+dist))
            distance[x] = cost + dist

    return distance[end]

x = min(dijik(1, v1)+dijik(v1, v2)+dijik(v2, n), dijik(1, v2)+dijik(v1, v2)+dijik(v1, n))
if x >= INF:
    print(-1)
else:
    print(x)
# 4 6
# 1 2 3
# 2 3 3
# 3 4 1
# 1 3 5
# 2 4 5
# 1 4 4
# 2 3