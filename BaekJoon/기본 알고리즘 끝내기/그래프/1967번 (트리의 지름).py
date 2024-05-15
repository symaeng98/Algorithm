from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def bfs(s):
    visited = [False] * (n+1)
    q = deque([(s, 0)])
    visited[s] = True
    max_node_distance = [0, 0]

    while q:
        x, dist = q.popleft()
        for g in graph[x]:
            if not visited[g[0]]:
                cost = dist + g[1]
                if cost > max_node_distance[1]:
                    max_node_distance[1] = cost
                    max_node_distance[0] = g[0]
                visited[g[0]] = True
                q.append((g[0], cost))

    return max_node_distance

v, dist = bfs(1)
x, result = bfs(v)
print(result)