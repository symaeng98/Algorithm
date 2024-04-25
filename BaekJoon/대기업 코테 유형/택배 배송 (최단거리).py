import heapq
INF = 1e9

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

hq = []
distance = [INF]*(n+1)
heapq.heappush(hq, (0, 1))
distance[1] = 0

while hq:
    dist, v = heapq.heappop(hq)
    if distance[v] < dist:
        continue
    for g in graph[v]:
        cost = dist + g[1]
        if cost < distance[g[0]]:
            distance[g[0]] = cost
            heapq.heappush(hq, (cost, g[0]))

print(distance[n])