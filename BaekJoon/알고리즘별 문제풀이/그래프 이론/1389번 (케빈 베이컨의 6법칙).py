import heapq

INF = 1e9
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

min_arr = []
for s in range(1, n+1):
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q, (0, s))

    while q:
        cost, v = heapq.heappop(q)
        for g in graph[v]:
            if cost + 1 < distance[g]:
                distance[g] = cost + 1
                heapq.heappush(q, (cost+1, g))

    min_arr.append((s, sum(distance[1:]) - distance[s]))

print(sorted(min_arr, key= lambda x:(x[1], x[0]))[0][0])