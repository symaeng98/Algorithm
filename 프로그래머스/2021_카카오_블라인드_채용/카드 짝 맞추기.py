from collections import deque
from itertools import permutations
import copy

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def solution(board, r, c):
    answer = 0
    all_card = []
    total_card_num = 0
    pair = [[] for _ in range(7)]
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                total_card_num = max(total_card_num, board[i][j])
                all_card.append((i, j))
                pair[board[i][j]].append((i, j))

    def xy_to_txy(graph, x, y, tx, ty):
        if (x, y) == (tx, ty):
            return 0
        q = deque([(0, x, y)])
        visited = {(x, y)}

        while q:
            cost, x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                mx = x
                my = y
                while True:
                    mx += dx[i]
                    my += dy[i]
                    if not (0 <= mx <= 3 and 0 <= my <= 3):
                        mx -= dx[i]
                        my -= dy[i]
                        break
                    elif graph[mx][my] != 0:
                        break

                if (nx, ny) == (tx, ty) or (mx, my) == (tx, ty):
                    return cost + 1

                if (0 <= nx <= 3 and 0 <= ny <= 3) and (nx, ny) not in visited:
                    q.append((cost+1, nx, ny))
                    visited.add((nx, ny))

                if (mx, my) not in visited:
                    q.append((cost+1, mx, my))
                    visited.add((mx, my))

    result = []
    def rec(order, index, now):
        if index == total_card_num:
            per = now
            tmp = copy.deepcopy(board)
            cost = 0
            now_r, now_c = r, c
            for i in range(len(per)//2):
                cost += xy_to_txy(tmp, now_r, now_c, per[i*2][0], per[i*2][1])
                now_r, now_c = per[i*2][0], per[i*2][1]
                cost += 1
                cost += xy_to_txy(tmp, now_r, now_c, per[i*2+1][0], per[i*2+1][1])
                now_r, now_c = per[i*2+1][0], per[i*2+1][1]
                cost += 1

                tmp[per[i*2+1][0]][per[i*2+1][1]] = 0
                tmp[per[i*2][0]][per[i*2][1]] = 0
            result.append(cost)
            return
        for i in range(total_card_num):
            if i == index:
                for a, b in [(0, 1), (1, 0)]:
                    now.append(pair[order[i]][a])
                    now.append(pair[order[i]][b])
                    rec(order, index+1, now)
                    now.pop()
                    now.pop()


    for per in permutations([i for i in range(1, total_card_num+1)]):
        rec(list(per), 0, [])

    return min(result)