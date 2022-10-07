INF = int(1e9)

n, m = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for i in range(1,n+1):
    graph[i][i] = 0

for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])

# for i in range(1,n+1):
#     for j in range(1, n+1):
#         if graph[i][j] == INF:
#             print("INF", end=" ")
#         else:
#             print(graph[i][j], end=" ")
#     print()

distance = graph[1][k]+graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)

# N의 범위 확인하지도 않고 플로이드 워셜 사용하면 안될 듯,,

# input
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5