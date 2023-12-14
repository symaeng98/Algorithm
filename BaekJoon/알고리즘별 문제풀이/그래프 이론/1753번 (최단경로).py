import heapq

INF = 1e9
v, e = map(int, input().split())
k = int(input())
distance = [INF]*(v+1)

graph = [[] for _ in range(v+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((w,v))

def dijik(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        for cost, vert in graph[now]:
            if dist+cost < distance[vert]:
                distance[vert] = dist+cost
                heapq.heappush(q, (dist+cost, vert))

dijik(k)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print("INF")
        continue
    print(distance[i])