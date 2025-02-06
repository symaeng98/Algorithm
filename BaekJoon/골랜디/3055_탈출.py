from collections import deque
# 09:56
r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
water_pos = []
gx, gy = -1, -1
des_x, des_y = -1, -1

for i in range(r):
    for j in range(c):
        if graph[i][j] == "*":
            water_pos.append((i, j))
        elif graph[i][j] == "S":
            gx, gy = i, j
        elif graph[i][j] == "D":
            des_x, des_y = i, j


water = [[-1]*c for _ in range(r)]
q = deque()
for i, j in water_pos:
    q.append((0, i, j))
    water[i][j] = 0

while q:
    cnt, x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] != "D" and graph[nx][ny] != "X":
                if water[nx][ny] == -1:
                    q.append((cnt+1, nx, ny))
                    water[nx][ny] = cnt+1

g_graph = [[-1]*c for _ in range(r)]
q = deque()
q.append((0, gx, gy))
g_graph[gx][gy] = 0
while q:
    cnt, x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] != "X" and (water[nx][ny] == -1 or water[nx][ny] > cnt+1):
                if g_graph[nx][ny] == -1:
                    q.append((cnt+1, nx, ny))
                    g_graph[nx][ny] = cnt+1

if g_graph[des_x][des_y] == -1:
    print("KAKTUS")
else:
    print(g_graph[des_x][des_y])


# 3 6
# D...*.
# .X.X..
# ....S.