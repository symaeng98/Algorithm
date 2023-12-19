from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def cnt(drown, x, y, num):
    if drown[x][y] != 0:
        return False
    q = deque()
    q.append((x, y))
    drown[x][y] = num
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and drown[nx][ny] == 0:
                drown[nx][ny] = num
                q.append((nx, ny))

    return True

max_cnt = 1
for h in range(0, 101):
    drown = [[0]*n for _ in range(n)]
    # drown 확인
    for i in range(n):
        for j in range(n):
            if board[i][j] <= h:
                drown[i][j] = -1

    # drown으로 개수
    num = 1
    for i in range(n):
        for j in range(n):
            if cnt(drown, i, j, num):
                num += 1
    max_cnt = max(max_cnt, num)


print(max_cnt-1)