import heapq

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))


INF = 1e9
distance = [INF]*(v+1)
def dijik(s):
    hq = []
    heapq.heappush(hq, (0, s))
    distance[s] = 0
    while hq:
        w, v = heapq.heappop(hq)
        for nw, nv in graph[v]:
            if distance[nv] > distance[v]+nw:
                distance[nv] = distance[v]+nw
                heapq.heappush(hq, (distance[nv], nv))


dijik(k)

for i, d in enumerate(distance):
    if i == 0:
        continue
    if d == INF:
        print("INF")
        continue
    print(d)

# 5 6
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6