from itertools import combinations


def dfs(graph, x, y, dx, dy):
    if graph[x][y] == 'S':
        return False
    if graph[x][y] == 'O':
        return True
    nx = x + dx
    ny = y + dy
    if 0 <= nx < len(graph) and 0 <= ny < len(graph):
        return dfs(graph, nx, ny, dx, dy)
    return True


N = int(input())
graph = [list(input().split()) for _ in range(N)]

empty = []
teacher = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == "X":
            empty.append((i,j))
        if graph[i][j] == "T":
            teacher.append((i,j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
flag = False
for comb in combinations(empty, 3):
    x1, y1 = comb[0][0], comb[0][1]
    x2, y2 = comb[1][0], comb[1][1]
    x3, y3 = comb[2][0], comb[2][1]
    graph[x1][y1] = "O"
    graph[x2][y2] = "O"
    graph[x3][y3] = "O"

    result = True
    for t in teacher:
        tx, ty = t[0], t[1]
        for i in range(4):
            if not dfs(graph, tx, ty, dx[i], dy[i]):
                result = False
    if result:
        print("YES")
        flag = True
        break

    graph[x1][y1] = "X"
    graph[x2][y2] = "X"
    graph[x3][y3] = "X"

if not flag:
    print("NO")
