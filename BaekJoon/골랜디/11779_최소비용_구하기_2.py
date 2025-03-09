import heapq

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

INF = 1e9
s, e = map(int, input().split())
parents = [i for i in range(n+1)]
distance = [INF]*(n+1)

q = []
heapq.heappush(q, (0, s))
distance[s] = 0
while q:
    cost, x = heapq.heappop(q)
    if cost > distance[x]:
        continue
    for v, c in graph[x]:
        if distance[v] > distance[x]+c:
            distance[v] = distance[x]+c
            parents[v] = x
            heapq.heappush(q, (distance[x]+c, v))

print(distance[e])
result = []
x = e
while x != s:
    result.append(x)
    x = parents[x]
result.append(s)
result.reverse()
print(len(result))
print(*result)
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