from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0 ,0]

def bfs(cnt, x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    graph[x][y] = cnt

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0 or visited[nx][ny]:
                    continue
                q.append((nx, ny))
                visited[nx][ny] = True
                graph[nx][ny] = cnt


cnt = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0 or visited[i][j]:
            continue
        bfs(cnt, i, j)
        cnt += 1

print(cnt-1)