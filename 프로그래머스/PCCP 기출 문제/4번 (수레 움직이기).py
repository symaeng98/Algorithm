from collections import deque
import copy

def solution(maze):
    answer = 0
    n = len(maze)
    m = len(maze[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    rx, ry, bx, by, rdx, rdy, bdx, bdy = 0, 0, 0, 0, 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                rx, ry = i, j
            elif maze[i][j] == 2:
                bx, by = i, j
            elif maze[i][j] == 3:
                rdx, rdy = i, j
            elif maze[i][j] == 4:
                bdx, bdy = i, j


    q = deque([(rx, ry, bx, by, 0, [(rx, ry)], [(bx, by)])])
    while q:
        rx, ry, bx, by, cnt, r_visited, b_visited = q.popleft()
        # print(rx, ry, bx, by, cnt, r_visited, b_visited)
        if rx == rdx and ry == rdy and bx == bdx and by == bdy:
            return cnt
        if rx == rdx and ry == rdy:
            for i in range(4):
                nbx = bx + dx[i]
                nby = by + dy[i]
                if 0 <= nbx < n and 0 <= nby < m and (nbx, nby) not in b_visited and maze[nbx][nby] != 5 and not (nbx == rx and nby == ry):
                    tmp_b_visited = copy.deepcopy(b_visited)
                    tmp_b_visited.append((nbx, nby))
                    q.append((rx, ry, nbx, nby, cnt+1, r_visited, tmp_b_visited))
        elif bx == bdx and by == bdy:
            for i in range(4):
                nrx = rx + dx[i]
                nry = ry + dy[i]
                if 0 <= nrx < n and 0 <= nry < m and (nrx, nry) not in r_visited and maze[nrx][nry] != 5 and not (nrx == bx and nry == by):
                    tmp_r_visited = copy.deepcopy(r_visited)
                    tmp_r_visited.append((nrx, nry))
                    q.append((nrx, nry, bx, by, cnt+1, tmp_r_visited, b_visited))
        else:
            for i in range(4):
                nrx = rx + dx[i]
                nry = ry + dy[i]
                if 0 <= nrx < n and 0 <= nry < m and (nrx, nry) not in r_visited and maze[nrx][nry] != 5:
                    for j in range(4):
                        nbx = bx + dx[j]
                        nby = by + dy[j]
                        if 0 <= nbx < n and 0 <= nby < m and (nbx, nby) not in b_visited and maze[nbx][nby] != 5 and not (nrx == bx and nry == by and nbx == rx and nby == ry) and not (nrx == nbx and nry == nby):
                            tmp_r_visited = copy.deepcopy(r_visited)
                            tmp_b_visited = copy.deepcopy(b_visited)
                            tmp_r_visited.append((nrx, nry))
                            tmp_b_visited.append((nbx, nby))
                            q.append((nrx, nry, nbx, nby, cnt+1, tmp_r_visited, tmp_b_visited))

    return answer