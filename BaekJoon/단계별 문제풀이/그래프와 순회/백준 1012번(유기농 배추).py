import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(x, y):
    if graph[x][y] == 0 or graph[x][y] == 2:
        return False
    graph[x][y] = 2
    for i in range(4):
        rx = x + dx[i]
        ry = y + dy[i]
        if rx < 0 or rx >= m or ry < 0 or ry >= n:
            continue
        if graph[rx][ry] == 1:
            dfs(rx, ry)
    return True


result = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
t = int(input())
for i in range(t):
    m, n, k = map(int, input().split(" "))
    graph = [[0] * n for _ in range(m)]
    for j in range(k):
        x, y = map(int, input().split(" "))
        graph[x][y] = 1

    for j in range(m):
        for k in range(n):
            if dfs(j,k):
                result += 1
    print(result)
    result = 0