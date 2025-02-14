from collections import deque

n, m = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
graph = [list(input()) for _ in range(n)]


def find_max_distance(x, y):
    distance = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((x, y, 0))
    distance[x][y] = 0

    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if distance[nx][ny] == -1 and graph[nx][ny] == "L":
                    q.append((nx, ny, cnt+1))
                    distance[nx][ny] = cnt+1

    result = 0
    for i in range(n):
        for j in range(m):
            result = max(result, distance[i][j])

    return result

result = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            result = max(result, find_max_distance(i, j))

print(result)