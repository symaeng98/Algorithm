import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

p1, p2 = map(int, input().split())
distance = [-1]*(n+1)


def dijik(s):
    INF = 1000000000
    # visited = [False]*(n+1)
    q = []
    heapq.heappush(q, (-INF, s))
    # visited[s] = True
    distance[s] = INF
    # cnt = 0
    while q:
        cost, x = heapq.heappop(q)
        if -cost < distance[x]:
            continue
        for v, c in graph[x]:
            tmp = min(-cost, c)
            if tmp <= distance[v]:
                continue
            heapq.heappush(q, (-tmp, v))
            distance[v] = tmp
        # print(q, -cost, x)
        # cnt += 1
        # if cnt == 5:
        #     break

    # print(distance)

dijik(p1)

print(distance[p2])

# 3 3
# 1 2 2
# 3 1 3
# 2 3 2
# 1 3


# 4 5
# 1 2 4
# 1 3 3
# 2 3 4
# 3 4 2
# 2 4 1
# 1 4