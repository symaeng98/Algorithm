import heapq
def solution(n, edge):
    INF = 1e9
    graph = [[] for _ in range(n+1)]
    distance = [INF]*(n+1)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    q = []
    distance[1] = 0
    heapq.heappush(q, (1, 0))

    while q:
        v, dist = heapq.heappop(q)
        if distance[v] < dist:
            continue

        cost = dist + 1
        for g in graph[v]:
            if cost < distance[g]:
                heapq.heappush(q, (g, cost))
                distance[g] = cost

    max_dist = max(distance[1:])
    cnt = 0
    for dist in distance:
        if dist == INF:
            continue
        if dist == max_dist:
            cnt += 1
    return cnt