from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
distance = [[[0, 0] for _ in range(m)] for _ in range(n)]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    distance[0][0][0] = 1
    while q:
        x, y, flag = q.popleft()
        if x == n-1 and y == m-1:
            return distance[x][y][flag]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0 and distance[nx][ny][flag] == 0:
                    q.append((nx, ny, flag))
                    distance[nx][ny][flag] = distance[x][y][flag] + 1
                elif board[nx][ny] == 1 and flag == 0:
                    q.append((nx, ny, 1))
                    distance[nx][ny][1] = distance[x][y][0] + 1
    return -1


print(bfs())
