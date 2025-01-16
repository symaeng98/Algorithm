from collections import deque

INF = 1e9
r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[INF]*c for _ in range(r)]
f_visited = [[INF]*c for _ in range(r)]
q = deque()
fq = deque()
for i in range(r):
    for j in range(c):
        if graph[i][j] == "J":
            q.append((i, j))
            visited[i][j] = 1
        elif graph[i][j] == "F":
            fq.append((i, j))
            f_visited[i][j] = 1

while fq:
    fx, fy = fq.popleft()
    for i in range(4):
        nx = fx + dx[i]
        ny = fy + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != "#":
            if f_visited[fx][fy]+1 < f_visited[nx][ny]:
                fq.append((nx, ny))
                f_visited[nx][ny] = f_visited[fx][fy]+1

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != "#":
            if visited[nx][ny] == INF and f_visited[nx][ny] > visited[x][y]+1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y]+1

# for i in range(r):
#     print(f_visited[i])
#
# print()
# for i in range(r):
#     print(visited[i])

result = INF
for i in range(r):
    for j in range(c):
        if i in [0, r-1] or j in [0, c-1]:
            result = min(result, visited[i][j])

if result == INF:
    print("IMPOSSIBLE")
else:
    print(result)

# 4 4
# ####
# #JF#
# #..#
# #..#