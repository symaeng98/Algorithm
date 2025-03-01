r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
ac_x = None
for i in range(r):
    for j in range(c):
        if not ac_x and graph[i][j] == -1:
            ac_x = i


def spread():
    munji = []
    for i in range(r):
        for j in range(c):
            if graph[i][j] != -1 and graph[i][j] != 0:
                munji.append((graph[i][j], i, j))

    add = []
    for i in range(len(munji)):
        mj, x, y = munji[i]
        spread_amount = mj // 5
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                add.append((spread_amount, nx, ny))
                graph[x][y] -= spread_amount

    for sa, x, y in add:
        graph[x][y] += sa


def up_rotate(acx):
    for i in range(acx-1, 0, -1):
        graph[i][0] = graph[i-1][0]
    for i in range(c-1):
        graph[0][i] = graph[0][i+1]
    for i in range(acx):
        graph[i][c-1] = graph[i+1][c-1]
    for i in range(c-1, 1, -1):
        graph[acx][i] = graph[acx][i-1]
    graph[acx][1] = 0



def down_rotate(acx):
    for i in range(acx+2, r-1):
        graph[i][0] = graph[i+1][0]
    for i in range(c-1):
        graph[r-1][i] = graph[r-1][i+1]
    for i in range(r-1, acx+1, -1):
        graph[i][c-1] = graph[i-1][c-1]
    for i in range(c-1, 1, -1):
        graph[acx+1][i] = graph[acx+1][i-1]
    graph[acx+1][1] = 0


for _ in range(t):
    spread()
    # for i in range(r):
    #     print(graph[i])
    # print()
    up_rotate(ac_x)
    # for i in range(r):
    #     print(graph[i])
    # print()
    down_rotate(ac_x)
    # for i in range(r):
    #     print(graph[i])
    # print()
    # print("___")


# for i in range(r):
#     print(graph[i])


result = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] != -1:
            result += graph[i][j]

print(result)


# 7 8 1
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0