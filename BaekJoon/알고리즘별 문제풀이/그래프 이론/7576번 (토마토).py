from collections import deque
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

q = deque()
cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            q.append((nx, ny))
            board[nx][ny] = board[x][y] + 1



result = -1
for b in board:
    if 0 in b:
        result = -1
        break
    result = max(result, max(b))

if result == -1:
    print(result)
else:
    print(result-1)

