import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
        elif graph[i][j] == 'B':
            bx, by = i, j

def bfs(rx, ry, bx, by):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append((rx, ry, bx, by, 0))
    visited = []
    visited.append((rx, ry, bx, by))

    while q:
        rx, ry, bx, by, cnt = q.popleft()
        if cnt > 10:
            print(-1)
            return
        if graph[rx][ry] == 'O':
            print(cnt)
            return
        for i in range(4):
            rnx, rny, bnx, bny = rx, ry, bx, by
            while True:
                rnx += dx[i]
                rny += dy[i]
                if graph[rnx][rny] == '#':
                    rnx -= dx[i]
                    rny -= dy[i]
                    break
                if graph[rnx][rny] == 'O':
                    break

            while True:
                bnx += dx[i]
                bny += dy[i]
                if graph[bnx][bny] == '#':
                    bnx -= dx[i]
                    bny -= dy[i]
                    break
                if graph[bnx][bny] == 'O':
                    break

            if graph[bnx][bny] == 'O':
                continue

            if rnx == bnx and rny == bny:
                if abs(rnx-rx) + abs(rny-ry) < abs(bnx-bx) + abs(bny-by):
                    bnx -= dx[i]
                    bny -= dy[i]
                else:
                    rnx -= dx[i]
                    rny -= dy[i]

            if (rnx, rny, bnx, bny) not in visited:
                q.append((rnx, rny, bnx, bny, cnt+1))
                visited.append((rnx, rny, bnx, bny))

    print(-1)
bfs(rx, ry, bx, by)