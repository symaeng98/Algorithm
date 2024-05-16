import heapq

def solution(n, s, a, b, fares):
    answer = 0
    INF = 1e9
    graph = [[] for _ in range(n+1)]
    for c,d,f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    def shortest(start):
        distance = [INF]*(n+1)
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, v = heapq.heappop(q)
            if dist > distance[v]:
                continue
            for g in graph[v]:
                cost = dist + g[1]
                if cost < distance[g[0]]:
                    distance[g[0]] = cost
                    heapq.heappush(q, (cost, g[0]))

        return distance

    together = shortest(s)
    result = []
    for i in range(1, n+1):
        alone = shortest(i)
        result.append(together[i] + alone[a] + alone[b])

    return min(result)