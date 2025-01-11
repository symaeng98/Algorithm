import heapq

INF = 1e9
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

a, b = map(int, input().split())
distance = [INF]*(n+1)

q = []
heapq.heappush(q, (0, a))
distance[a] = 0

while q:
    cost, x = heapq.heappop(q)
    if distance[x] < cost:
        continue
    for g in graph[x]:
        dist, v = g[0], g[1]
        if distance[v] > dist + distance[x]:
            distance[v] = dist + distance[x]
            heapq.heappush(q, (distance[v], v))

# print(distance)
print(distance[b])
# 5
# 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5