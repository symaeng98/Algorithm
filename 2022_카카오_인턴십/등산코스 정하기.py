import heapq

INF = 1e9
def bfs(graph, summits, gates, n):
    q = []
    summits.sort()
    summit_set = set(summits)
    distance = [INF] * (n+1)
    for gate in gates:
        heapq.heappush(q, (0, gate))
        distance[gate] = 0

    while q:
        intensity, v = heapq.heappop(q)
        if v in summit_set or intensity > distance[v]:
            continue

        for g, w in graph[v]:
            now_intensity = max(intensity, w)
            if distance[g] > now_intensity:
                distance[g] = now_intensity
                heapq.heappush(q, (now_intensity, g))

    result = [INF, INF]
    for summit in summits:
        if distance[summit] < result[1]:
            result[0] = summit
            result[1] = distance[summit]
    return result


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for a, b, w in paths:
        graph[a].append((b, w))
        graph[b].append((a, w))

    answer_summit, answer_intensity = bfs(graph, summits, gates, n)

    return [answer_summit, answer_intensity]

print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))
print(solution(2, [[1, 2, 10]], [1], [2]))