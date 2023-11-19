n = int(input())
graph = []
visited = [[False] * n for _ in range(n)]
num = 0
cnt = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(n):
    l = list(map(int, input()))
    graph.append(l)


def dfs(x, y):
    global num
    if graph[x][y] == 0 or visited[x][y]:
        return
    visited[x][y] = True
    num += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 0:
            continue
        if not visited[nx][ny]:
            dfs(nx, ny)

numArr = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
        dfs(i, j)
        if num != 0:
            numArr.append(num)
            num = 0

print(cnt)
numArr.sort()
for n in numArr:
    print(n)
