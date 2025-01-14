import sys
sys.setrecursionlimit(10**4)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def process():
    q = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if graph[nx][ny] == 0:
                        cnt += 1

                q.append((i, j, cnt))

    for x, y, cnt in q:
        if graph[x][y] > cnt:
            graph[x][y] -= cnt
        else:
            graph[x][y] = 0


def dfs(x, y, visited, cnt):
    if visited[x][y] != 0:
        return
    visited[x][y] = cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] != 0 and not visited[nx][ny]:
                dfs(nx, ny, visited, cnt)


def check():
    result = 1
    while True:
        flag = False
        for i in range(n):
            for j in range(m):
                if graph[i][j] != 0:
                    flag = True
        if not flag:
            return 0

        process()
        visited = [[0]*m for _ in range(n)]
        cnt = 1
        for i in range(n):
            for j in range(m):
                if graph[i][j] != 0:
                    dfs(i, j, visited, cnt)
                    cnt += 1
        # print(graph)
        # print(visited)
        for i in range(n):
            for j in range(m):
                if visited[i][j] > 1:
                    return result

        result += 1

print(check())
# 5 7
# 0 0 0 0 0 0 0
# 0 2 4 5 3 0 0
# 0 3 0 2 5 2 0
# 0 7 6 2 4 0 0
# 0 0 0 0 0 0 0