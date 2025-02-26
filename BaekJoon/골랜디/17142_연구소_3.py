import copy
from collections import deque
from itertools import combinations
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

viruses = []
INF = 1e9
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            viruses.append((i, j))
            graph[i][j] = -3
        if graph[i][j] == 0:
            graph[i][j] = INF
        if graph[i][j] == 1:
            graph[i][j] = -2
# INF: 가능, -2: 벽, -3: 비활성 바이러스
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def cnt(board, comb):
    q = deque()
    for i, j in comb:
        board[i][j] = 0
        q.append((0, i, j))

    nonactivate_virus = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == -3:
                nonactivate_virus.append((i, j))

    while q:
        cnt, x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == INF or board[nx][ny] == -3:
                    board[nx][ny] = cnt+1
                    q.append((cnt+1, nx, ny))

    # for i in range(n):
    #     print(board[i])
    # print()

    answer = -1
    for i in range(n):
        for j in range(n):
            if board[i][j] > answer and (i, j) not in nonactivate_virus:
                answer = board[i][j]

    return answer


result = INF
for comb in combinations(viruses, m):
    tmp = copy.deepcopy(graph)
    result = min(result, cnt(tmp, comb))

if result == INF:
    print(-1)
else:
    print(result)

# 7 3
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 2 0 1 1
# 0 1 0 0 0 0 0
# 2 1 0 0 0 0 2