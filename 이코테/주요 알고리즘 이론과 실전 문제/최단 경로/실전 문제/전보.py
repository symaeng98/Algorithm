import heapq

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

def dijikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dis, v = heapq.heappop(q)
        if distance[v] < dis:
            continue
        for g in graph[v]:
            cost = dis + g[1]
            if cost < distance[g[0]]:
                distance[g[0]] = cost
                heapq.heappush(q,(cost,g[0]))

dijikstra(c)

cnt = 0
max_dis = -1
for d in distance:
    if d != INF:
        cnt += 1
        max_dis = max(max_dis,d)
print(cnt-1, max_dis)

# 처음에 n, m, c 를 입력 받고, 그 뒤의 간선 정보를 a, b, c로 입력을 받아서 c가 덮어씌워졌다,,ㅎ