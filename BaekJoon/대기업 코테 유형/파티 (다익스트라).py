import heapq

INF = 1e9
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

result = [[] for _ in range(n+1)]

for i in range(1, n+1):
    q = [(0, i)]
    distance = [INF]*(n+1)
    distance[i] = 0

    while q:
        dist, v = heapq.heappop(q)
        if distance[v] < dist:
            continue

        for k, c in graph[v]:
            cost = dist + c
            if cost < distance[k]:
                distance[k] = cost
                heapq.heappush(q, (cost, k))

    result[i].extend(distance)


max_time = -1
for i in range(1, n+1):
    max_time = max(max_time, result[i][x] + result[x][i])

print(max_time)