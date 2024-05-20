from collections import deque
from itertools import permutations
import copy

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def solution(board, r, c):
    answer = 0
    pair = [[] for _ in range(7)]
    total_card_num = 0
    for k in range(1, 7):
        for i in range(4):
            for j in range(4):
                if board[i][j] == k:
                    total_card_num = max(total_card_num, k)
                    pair[k].append((i, j))
    print(total_card_num)

    def xy_to_txy(board, x, y, tx, ty):
        distance = [[0]*4 for _ in range(4)]
        distance[x][y] = 0
        for i in range(4):
            for j in range(4):
                distance[i][j] = abs(i-x) + abs(j-y)

        q = deque()
        q.append((0, x, y))
        visited = [(x, y)]
        while q:
            cost, x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                mx = x + dx[i]
                my = y + dy[i]
                if 0 <= mx < 4 and 0 <= my < 4:
                    if (mx, my) not in visited:
                        visited.append((mx, my))
                        distance[mx][my] = cost + 1
                        q.append((cost+1, mx, my))
                while True:
                    if 0 <= nx < 4 and 0 <= ny < 4:
                        if board[nx][ny] != 0:
                            break
                        nx += dx[i]
                        ny += dy[i]
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                # if nx == x and ny == y:
                #     continue
                if (nx, ny) not in visited:
                    visited.append((nx, ny))
                    distance[nx][ny] = cost + 1
                    q.append((cost+1, nx, ny))
        # print(distance)
        return distance[tx][ty]

    print(pair)
    for per in permutations([i for i in range(1, total_card_num+1)]):
        result = []
        tmp = copy.deepcopy(board)
        cost = 0
        for now in per:
            p1 = xy_to_txy(tmp, r, c, pair[now][0][0], pair[now][0][1])
            p2 = xy_to_txy(tmp, r, c, pair[now][1][0], pair[now][1][1])
            print(p1, p2)
            if p1 < p2:
                cost += p1
                r, c = pair[now][0][0], pair[now][0][1]

                cost += 1
                cost += xy_to_txy(tmp, r, c, pair[now][1][0], pair[now][1][1])
                r, c = pair[now][1][0], pair[now][1][1]
                cost += 1
                tmp[pair[now][0][0]][pair[now][0][1]] = 0
                tmp[pair[now][1][0]][pair[now][1][1]] = 0
            else:
                cost += p2
                r, c = pair[now][1][0], pair[now][1][1]

                cost += 1
                cost += xy_to_txy(tmp, r, c, pair[now][0][0], pair[now][0][1])
                r, c = pair[now][0][0], pair[now][0][1]
                cost += 1
                tmp[pair[now][0][0]][pair[now][0][1]] = 0
                tmp[pair[now][1][0]][pair[now][1][1]] = 0

        result.append(cost)

    print(result)
    return result