from collections import deque
INF = 1e9
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            current_x, current_y = i, j
            board[i][j] = 0

size_cnt = 0
current_size = 2

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    dist = [[-1]*n for _ in range(n)]
    dist[current_x][current_y] = 0
    q = deque()
    q.append((current_x, current_y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1 and board[nx][ny] <= current_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist

def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= board[i][j] < current_size:
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist


result = 0
ate = 0

while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    current_x, current_y = value[0], value[1]
    result += value[2]

    board[current_x][current_y] = 0
    ate += 1

    if ate >= current_size:
        current_size += 1
        ate = 0