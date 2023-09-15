n = int(input())
m = int(input())
INF = 1e9

dist = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

for i in range(1, n+1):
    for d in dist[i][1:]:
        if d == INF:
            print(0, end=" ")
        else:
            print(d, end=" ")
    print()