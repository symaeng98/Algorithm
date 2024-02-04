import heapq

def dijik(v):
    result = [INF]*(n+1)
    q = []
    result[v] = 0
    heapq.heappush(q, (0, v))

    while q:
        dist, v = heapq.heappop(q)
        for cost, x in graph[v]:
            if cost + dist < result[x]:
                result[x] = cost + dist
                heapq.heappush(q, (cost + dist, x))

    return result

INF = 1e9
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())

distance_one_to_v = dijik(1)
distance_v1_to_v2 = dijik(v1)
distance_n_to_v = dijik(n)

if distance_v1_to_v2[v2] == INF:
    print(-1)
elif distance_one_to_v[v1] == INF and distance_one_to_v[v2] == INF:
    print(-1)
elif distance_n_to_v[v1] == INF and distance_n_to_v[v2] == INF:
    print(-1)
else:
    v1_to_v2 = distance_v1_to_v2[v2]
    result = min((distance_one_to_v[v1] + distance_n_to_v[v2]), (distance_one_to_v[v2] + distance_n_to_v[v1])) + v1_to_v2
    print(result)

