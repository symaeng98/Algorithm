n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

while True:
    if board[x][y] == 0:
        cnt += 1
        board[x][y] = 2

    available = False
    for i in range(4):
        d = (d+3)%4
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 0:
                x = nx
                y = ny
                available = True
                break
    if available:
        continue
    else:
        nx = x - dx[d]
        ny = y - dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] != 1:
                x = nx
                y = ny
                continue
            break

print(cnt)