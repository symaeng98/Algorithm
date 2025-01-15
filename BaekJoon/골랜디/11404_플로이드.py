n = int(input())
m = int(input())
INF = 1e9
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)


for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                graph[i][j] = 0
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(n+1):
    if i == 0:
        continue
    for j in range(n+1):
        if j == 0:
            continue
        if graph[i][j] == INF:
            graph[i][j] = 0
        print(graph[i][j], end=" ")
    print()
# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4