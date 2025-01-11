from collections import deque

m, n, h = map(int, input().split())
graph = [[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        graph[i].append(list(map(int, input().split())))


q = deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                q.append((1, k, i, j))

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while q:
    day, z, x, y = q.popleft()
    for i in range(6):
        nx = dx[i] + x
        ny = dy[i] + y
        nz = dz[i] + z
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = day+1
                q.append((day+1, nz, nx, ny))

is_valid = True
max_day = -1
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                is_valid = False
            max_day = max(max_day, graph[k][i][j])

if is_valid:
    print(max_day-1)
else:
    print(-1)

# 5 3 2
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 0