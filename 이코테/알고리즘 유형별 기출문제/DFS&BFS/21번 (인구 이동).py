from collections import deque

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(i, j, ind):
    nation = [(i, j)]
    q = deque()
    q.append((i, j))
    union[i][j] = ind
    nationCnt = 1
    nationSum = graph[i][j]
    while q:
        x, y = q.popleft()
        for ind in range(4):
            nx = x + dx[ind]
            ny = y + dy[ind]
            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1 and L <= abs(graph[nx][ny]-graph[x][y]) <= R:
                union[nx][ny] = ind
                q.append((nx, ny))
                nation.append((nx, ny))
                nationCnt += 1
                nationSum += graph[nx][ny]
    for n in nation:
        graph[n[0]][n[1]] = nationSum // nationCnt
    return nationCnt

day = 0
while True:
    union = [[-1]*N for _ in range(N)]
    ind = 0
    for i in range(N):
        for j in range(N):
            if union[i][j] == -1:
                bfs(i, j, ind)
                ind += 1

    if ind == N * N:
        break
    day += 1

print(day)