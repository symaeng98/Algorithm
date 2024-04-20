from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
zeros = []

sx, sy = -1, -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            sx, sy = i, j
        elif graph[i][j] == 0:
            zeros.append((i, j))

result = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
q = deque()
q.append((0, sx, sy))
visited[sx][sy] = True

while q:
    dist, x, y = q.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            result[nx][ny] = result[x][y] + 1
            q.append((result[nx][ny]+1, nx, ny))

for i in range(n):
    for j in range(m):
        if result[i][j] == 0 and graph[i][j] == 1:
            result[i][j] = -1

for i in range(n):
    for j in range(m):
        print(result[i][j], end=" ")
    print()