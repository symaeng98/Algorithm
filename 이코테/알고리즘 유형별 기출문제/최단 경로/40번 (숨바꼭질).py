import heapq
INF = 1e9

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

q = []
heapq.heappush(q, (1,0))
distance[1] = 0

while q:
    s, dist = heapq.heappop(q)
    if distance[s] < dist:
        continue
    for v in graph[s]:
        cost = dist + v[1]
        if cost < distance[v[0]]:
            distance[v[0]] = cost
            heapq.heappush(q, (v[0],cost))

max_node = 0
max_distance = 0
result = []
for i in range(1, n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance, len(result))