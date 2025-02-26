#2:38
import sys
input = sys.stdin.readline
sys.setrecursionlimit(250000)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if cnt[x][y] != 0:
        return cnt[x][y]

    cnt[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > graph[x][y]:
            cnt[x][y] = max(cnt[x][y], dfs(nx, ny) + 1)
    return cnt[x][y]


cnt = [[0]*n for _ in range(n)]
result = -1
for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))

print(result)
# 4
# 14 9 12 10
# 1 11 5 4
# 7 15 2 13
# 6 3 16 8