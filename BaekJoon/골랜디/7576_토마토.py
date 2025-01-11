from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j, 1))
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    x, y, cnt = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            graph[nx][ny] = cnt+1
            q.append((nx, ny, cnt+1))

result = 0
fail = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            fail = True
        if result < graph[i][j]:
            result = graph[i][j]

if fail:
    print(-1)
else:
    print(result-1)

# 6 4
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1