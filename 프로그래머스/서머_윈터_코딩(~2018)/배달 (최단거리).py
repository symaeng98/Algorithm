import heapq
def solution(N, road, K):
    INF = 1e9
    graph = [[] for _ in range(N+1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    q = []
    distance = [INF]*(N+1)
    distance[1] = 0
    heapq.heappush(q, (0, 1))
    while q:
        dist, v = heapq.heappop(q)
        if dist > distance[v]:
            continue
        for g in graph[v]:
            cost = dist + g[1]
            if cost < distance[g[0]]:
                distance[g[0]] = cost
                heapq.heappush(q, (cost, g[0]))

    cnt = 0
    for d in distance:
        if d <= K:
            cnt += 1

    return cnt