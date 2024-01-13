from collections import deque

m, n, k = map(int, input().split())
board = [[1]*n for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y, cnt):
    if board[x][y] != 1:
        return False

    q = deque()
    q.append((x, y))
    board[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 1:
                q.append((nx, ny))
                board[nx][ny] = cnt
    return True


for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(m-y2, m-y1):
        for j in range(x1, x2):
            board[i][j] = 0

cnt = 2
for i in range(m):
    for j in range(n):
        if bfs(i, j, cnt):
            cnt += 1

result = [0]*(cnt)
for i in range(m):
    for j in range(n):
        result[board[i][j]] += 1

print(cnt-2)
for r in sorted(result[2:cnt]):
    print(r, end=" ")