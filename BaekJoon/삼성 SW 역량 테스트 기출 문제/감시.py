import copy

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]],
]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

cctv = []
for i in range(n):
    for j in range(m):
        if board[i][j] in [1, 2, 3, 4, 5]:
            cctv.append((board[i][j], i, j))

result = 1e9
def dfs(index, graph):
    global result
    if index == len(cctv):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    cnt += 1
        result = min(result, cnt)
        return

    tmp = copy.deepcopy(graph)
    c, x, y = cctv[index]
    for d in direction[c]:
        for i in d:
            nx = x
            ny = y
            while True:
                nx += dx[i]
                ny += dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if tmp[nx][ny] == 6:
                        break
                    if tmp[nx][ny] == 0:
                        tmp[nx][ny] = -1
                else:
                    break
        dfs(index+1, tmp)
        tmp = copy.deepcopy(graph)

dfs(0, board)
print(result)