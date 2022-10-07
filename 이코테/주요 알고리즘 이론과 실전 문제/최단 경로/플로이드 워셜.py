INF = int(1e9)
n = int(input())
m = int(input())

graph = [[INF for _ in range(n+1)]for _ in range(n+1)]

for i in range(1, m+1):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, n+1):
    graph[i][i] = 0

for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("INF",end=" ")
        else:
            print(graph[i][j],end=" ")
    print()
## input
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2