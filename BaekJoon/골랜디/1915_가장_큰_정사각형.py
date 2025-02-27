n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            continue
        if 0 <= i-1 < n and 0 <= j-1 < m:
            graph[i][j] = min(graph[i-1][j], graph[i][j-1], graph[i-1][j-1])+1


result = -1
for i in range(n):
    for j in range(m):
        result = max(result, graph[i][j])

print(result**2)



# 4 10
# 0001111100
# 0001111100
# 0000111100
# 0000111100