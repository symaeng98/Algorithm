from collections import deque
t = int(input())
INF = 1e9
for _ in range(t):
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    n = int(input())
    sx, sy = map(int, input().split())
    ax, ay = map(int, input().split())
    dist = [[0]*n for _ in range(n)]

    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    dist[sx][sy] = 0
    print(dist[ax][ay])