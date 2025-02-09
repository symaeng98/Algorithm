# 10:40
r, c, m = map(int, input().split())
graph = [[None]*(c+1) for _ in range(r+1)]
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]
sharks = []
for _ in range(m):
    i, j, s, d, z = map(int, input().split())
    graph[i][j] = (s, d, z)
    sharks.append((i, j))
result = 0
for human in range(1, c+1):
    for i in range(1, r+1):
        if graph[i][human]:
            s, d, z = graph[i][human]
            graph[i][human] = None
            # print(i, human)
            result += z
            break

    sharks_tmp = []
    # print("이동 전", graph)
    for x, y in sharks:
        if not graph[x][y]:
            continue
        s, d, z = graph[x][y]
        graph[x][y] = None
        # 이동
        # print("이동 전 x, y", x, y, s, d)
        if d == 1 or d == 2:
            s = s % ((r-1)*2)
        else:
            s = s % ((c-1)*2)
        for _ in range(s):
            nx = dx[d]+x
            ny = dy[d]+y
            # print("nx, ny", nx, ny, d)
            if 1 <= nx < r+1 and 1 <= ny < c+1:
                x = nx
                y = ny
            else:
                if d == 1:
                    d = 2
                    x += 1
                elif d == 2:
                    d = 1
                    x -= 1
                elif d == 3:
                    d = 4
                    y -= 1
                elif d == 4:
                    d = 3
                    y += 1
        # print("첫 여기니")
        # print("이동 후 x, y", x, y, s, d)

        # print("이동 후", x, y, d)
        sharks_tmp.append((x, y, s, d, z))
    # print("이동 종료")
    for i, j, s, d, z in sharks_tmp:
        if graph[i][j]:
            if graph[i][j][2] < z:
                graph[i][j] = (s, d, z)
        else:
            graph[i][j] = (s, d, z)

    for i in range(1, r+1):
        for j in range(1, c+1):
            if graph[i][j]:
                sharks.append((i, j))
                # print("상어", i, j)

    # print("갱신 후", graph)

print(result)

# 4 6 8
# 4 1 3 3 8
# 1 3 5 2 9
# 2 4 8 4 1
# 4 5 0 1 4
# 3 3 1 2 7
# 1 5 8 4 3
# 3 6 2 1 2
# 2 2 2 3 5