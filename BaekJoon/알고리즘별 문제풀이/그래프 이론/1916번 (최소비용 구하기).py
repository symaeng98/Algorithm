import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))
s, e = map(int, input().split())

INF = 1e9
distance = [INF]*(n+1)
def dijik(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, v = heapq.heappop(q)
        if distance[v] < dist:
            continue
        for cost, x in graph[v]:
            dist = cost + distance[v]
            if distance[x] > dist:
                distance[x] = dist
                heapq.heappush(q, (dist, x))

dijik(s)

print(distance[e])