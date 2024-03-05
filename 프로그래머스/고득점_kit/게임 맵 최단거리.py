from collections import deque
INF = 1e9
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                maps[i][j] = INF

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append((1, 0, 0))
    maps[0][0] = 1
    while q:
        cnt, x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] != 0:
                    if cnt + 1 < maps[nx][ny]:
                        maps[nx][ny] = cnt + 1
                        q.append((cnt+1, nx, ny))

    answer = maps[n-1][m-1]

    if answer == INF:
        return -1
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))