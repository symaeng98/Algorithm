from collections import deque

m, n, h = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

tomatoes = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                tomatoes.append((i, j, k))
dx = [0, 0, 0, 0, 1, -1]
dy = [1, -1, 0, 0, 0, 0,]
dz = [0, 0, 1, -1, 0, 0]

while tomatoes:
    z, x, y = tomatoes.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
            if board[nz][nx][ny] == 0:
                board[nz][nx][ny] = board[z][x][y] + 1
                tomatoes.append((nz, nx, ny))


flag = False
day = -1
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 0:
                flag = True
                break
            if day < board[i][j][k]:
                day = board[i][j][k]
if flag:
    print(-1)
else:
    print(day-1)

