import copy

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

d_map = {
    1: [[(0, 1)], [(1, 0)], [(-1, 0)], [(0, -1)]],
    2: [[(0, 1), (0, -1)], [(-1, 0), (1, 0)]],
    3: [[(0, 1), (-1, 0)], [(1, 0), (0, 1)], [(0, -1), (1, 0)], [(-1, 0), (0, -1)]],
    4: [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)],
        [(0, 1), (1, 0), (0, -1)], [(-1, 0), (0, -1), (1, 0)]],
    5: [[(0, 1), (0, -1), (-1, 0), (1, 0)]],
}

cctvs = []
for i in range(n):
    for j in range(m):
        if 1 <= graph[i][j] <= 5:
            cctvs.append((i, j))

result = 100
def dfs(index):
    global result, graph
    if index == len(cctvs):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    cnt += 1
        # for i in range(n):
        #     print(graph[i])
        # print()
        result = min(result, cnt)
        return

    x, y = cctvs[index][0], cctvs[index][1]
    for dxdy in d_map[graph[x][y]]:
        # print(x, y, dxdy)
        tmp = copy.deepcopy(graph)
        for dx, dy in dxdy:
            tx, ty = x, y
            while True:
                nx = tx + dx
                ny = ty + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 6:
                        break
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = -1
                    tx = nx
                    ty = ny
                    continue
                break

        dfs(index+1)
        graph = tmp


dfs(0)
print(result)
