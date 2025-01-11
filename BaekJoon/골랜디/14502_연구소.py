from itertools import combinations
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

empty = []
virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i, j))
        if graph[i][j] == 2:
            virus.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
max_cnt = 0
for comb in combinations(empty, 3):
    for i, j in comb:
        graph[i][j] = 1

    q = deque()
    q.extend(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append((nx, ny))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    max_cnt = max(max_cnt, cnt)
    for i, j in empty:
        graph[i][j] = 0

print(max_cnt)

# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0