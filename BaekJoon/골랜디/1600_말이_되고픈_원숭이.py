from collections import deque

k = int(input())
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
INF = 1e9
distance = [[[INF]*m for _ in range(n)] for _ in range(k+1)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
hx = [1, 1, -1, -1, 2, 2, -2, -2]
hy = [2, -2, 2, -2, 1, -1, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y, 0, 0))
    distance[0][x][y] = 0

    while q:
        x, y, horse, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 1 and distance[horse][nx][ny] == INF:
                    distance[horse][nx][ny] = cnt+1
                    q.append((nx, ny, horse, cnt+1))
        if horse < k:
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] != 1 and distance[horse+1][nx][ny] == INF:
                        distance[horse+1][nx][ny] = cnt+1
                        q.append((nx, ny, horse+1, cnt+1))

bfs(0, 0)

result = INF
for p in range(k+1):
    if result > distance[p][n-1][m-1]:
        result = distance[p][n-1][m-1]
if result == INF:
    print(-1)
else:
    print(result)
# 1
# 4 4
# 0 0 0 0
# 1 0 0 0
# 0 0 1 0
# 0 1 0 0