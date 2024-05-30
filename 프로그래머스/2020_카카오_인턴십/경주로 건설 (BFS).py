from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
def solution(board):
    n = len(board)
    answer = 0
    result = 1e9
    visited = [[[False]*4 for _ in range(n)] for _ in range(n)]
    q = deque()
    visited[0][0][0] = True
    visited[0][0][3] = True
    if board[1][0] == 0:
        # i, j, direction, dist, cor
        q.append((1, 0, 0, 1, 0))
    if board[0][1] == 0:
        q.append((0, 1, 3, 1, 0))

    while q:
        x, y, direction, dist, cor = q.popleft()
        visited[x][y][direction] = True
        if x == n-1 and y == n-1:
            result = min(result, dist*100 + cor*500)
            print(result)
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1 and not visited[nx][ny][i]:

                if i == direction:
                    q.append((nx, ny, i, dist+1, cor))
                else:
                    q.append((nx, ny, i, dist+1, cor+1))

    return result