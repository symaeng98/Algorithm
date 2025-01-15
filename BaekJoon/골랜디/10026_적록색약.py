from collections import deque

n = int(input())
graph = [list(input()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs_normal(x, y, cnt, visited):
    g = graph[x][y]
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] == g:
                    visited[nx][ny] = cnt
                    q.append((nx, ny))


def grouping_normal():
    visited = [[0]*n for _ in range(n)]
    cnt = 1
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs_normal(i, j, cnt, visited)
                cnt += 1
    return cnt-1


normal_cnt = grouping_normal()
for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"

abnormal_cnt = grouping_normal()

print(normal_cnt, abnormal_cnt)

# 5
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR