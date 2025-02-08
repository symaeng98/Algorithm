import heapq

INF = 1e9
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijik(s):
    distance = [INF]*(n+1)
    hq = []
    heapq.heappush(hq, (0, s))
    distance[s] = 0

    while hq:
        dist, v = heapq.heappop(hq)
        if distance[v] < dist:
            continue

        for gv, cost in graph[v]:
            if distance[gv] > distance[v]+cost:
                distance[gv] = distance[v]+cost
                heapq.heappush(hq, (distance[v]+cost, gv))

    return distance


result = [0]*(n+1)
for i in range(1, n+1):
    go_to_party = dijik(i)[x]
    come_back_home = dijik(x)[i]
    result[i] += go_to_party + come_back_home

print(max(result))