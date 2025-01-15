import copy
from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, cnt, visited):
    q = deque()
    q.append((x, y))
    sum_value = graph[x][y]
    group_list = [(x, y)]
    visited[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    visited[nx][ny] = cnt
                    sum_value += graph[nx][ny]
                    group_list.append((nx, ny))
                    q.append((nx, ny))

    for x, y in group_list:
        graph[x][y] = sum_value // len(group_list)

    # print(group_list, sum_value, nation_cnt)
    # print(visited)


cnt = 0
while True:
    g_copy = copy.deepcopy(graph)
    group_cnt = 1
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i, j, group_cnt, visited)
                group_cnt += 1

    if g_copy == graph:
        break
    cnt += 1

print(cnt)

# 2 20 50
# 50 30
# 20 40