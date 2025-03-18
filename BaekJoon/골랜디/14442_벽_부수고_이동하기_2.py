from collections import deque

n, m, k = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
distance = [[[0]*m for _ in range(n)] for _ in range(k+1)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
q.append((0, 0, 0, 1))
distance[0][0][0] = 1
while q:
    x, y, wall_break, cnt = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                if distance[wall_break][nx][ny] == 0:
                    distance[wall_break][nx][ny] = cnt+1
                    q.append((nx, ny, wall_break, cnt+1))
            else:
                if wall_break < k and distance[wall_break+1][nx][ny] == 0:
                    distance[wall_break+1][nx][ny] = cnt+1
                    q.append((nx, ny, wall_break+1, cnt+1))

result = 10000000
for l in range(k+1):
    x = distance[l][n-1][m-1]
    if x == 0:
        continue
    result = min(result, x)

if result == 10000000:
    print(-1)
else:
    print(result)






# 6 4 1
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000