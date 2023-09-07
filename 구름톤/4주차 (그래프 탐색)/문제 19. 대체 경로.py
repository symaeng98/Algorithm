import heapq

INF = 1e9
n, m, s, e = map(int, input().split())

# 초기화
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dijikstra(start, construction, distance):
    q = []
    heapq.heappush(q, (1, start))
    distance[start] = 1
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = distance[now] + 1
            if i == construction:
                continue
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))


for i in range(1,n+1):
    distance = [INF] * (n + 1)
    if s == i or e == i:
        print(-1)
        continue
    dijikstra(s, i, distance)
    if distance[e] == INF:
        print(-1)
        continue
    print(distance[e])