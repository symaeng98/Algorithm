from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j
board[rx][ry] = '.'
board[bx][by] = '.'

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
            return -1
        if board[rx][ry] == "O":
            return cnt
        for i in range(4):
            nrx, nry, nbx, nby = rx, ry, bx, by
            while True:
                nrx += dx[i]
                nry += dy[i]
                if board[nrx][nry] == "#":
                    nrx -= dx[i]
                    nry -= dy[i]
                    break
                elif board[nrx][nry] == ".":
                    continue
                elif board[nrx][nry] == "O":
                    break

            while True:
                nbx += dx[i]
                nby += dy[i]
                if board[nbx][nby] == "#":
                    nbx -= dx[i]
                    nby -= dy[i]
                    break
                elif board[nbx][nby] == ".":
                    continue
                elif board[nbx][nby] == "O":
                    break

            if board[nbx][nby] == "O":
                continue

            if nrx == nbx and nry == nby:
                if abs(nrx-rx) + abs(nry-ry) < abs(nbx-bx) + abs(nby-by):
                    nbx -= dx[i]
                    nby -= dy[i]
                else:
                    nrx -= dx[i]
                    nry -= dy[i]

            if (nrx, nry, nbx, nby) not in visited:
                q.append((nrx, nry, nbx, nby, cnt+1))
                visited.append((nrx, nry, nbx, nby))

    return -1

print(bfs(rx, ry, bx, by))





# from collections import deque
#
# n, m = map(int, input().split())
# board = [list(input()) for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         if board[i][j] == 'R':
#             rx, ry = i, j
#         elif board[i][j] == 'B':
#             bx, by = i, j
#
#
# def bfs(rx, ry, bx, by):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, 1, -1]
#     q = deque()
#     q.append((rx, ry, bx, by, 0))
#     visited = []
#     visited.append((rx, ry, bx, by))
#
#     while q:
#         rx, ry, bx, by, cnt = q.popleft()
#         if cnt > 10:
#             print(-1)
#             return
#         if board[rx][ry] == "O":
#             print(cnt)
#             return
#         for i in range(4):
#             nrx, nry, nbx, nby = rx, ry, bx, by
#             while True:
#                 nrx += dx[i]
#                 nry += dy[i]
#                 if board[nrx][nry] == "#":
#                     nrx -= dx[i]
#                     nry -= dy[i]
#                     break
#                 elif board[nrx][nry] == ".":
#                     continue
#                 elif board[nrx][nry] == "O":
#                     break
#
#             while True:
#                 nbx += dx[i]
#                 nby += dy[i]
#                 if board[nbx][nby] == "#":
#                     nbx -= dx[i]
#                     nby -= dy[i]
#                     break
#                 elif board[nbx][nby] == ".":
#                     continue
#                 elif board[nbx][nby] == "O":
#                     break
#
#             if board[nbx][nby] == "O":
#                 continue
#
#             if nrx == nbx and nry == nby:
#                 if abs(nrx-rx) + abs(nry-ry) < abs(nbx-bx) + abs(nby-by):
#                     nbx -= dx[i]
#                     nby -= dy[i]
#                 else:
#                     nrx -= dx[i]
#                     nry -= dy[i]
#
#             if (nrx, nry, nbx, nby) not in visited:
#                 q.append((nrx, nry, nbx, nby, cnt+1))
#                 visited.append((nrx, nry, nbx, nby))
#     print(-1)
#
# bfs(rx, ry, bx, by)