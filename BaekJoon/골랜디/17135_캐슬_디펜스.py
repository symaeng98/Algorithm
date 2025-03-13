import copy
from collections import deque
from itertools import combinations
#1:55
n, m, d = map(int, input().split())
q = deque()
for _ in range(n):
    q.append(list(map(int, input().split())))

max_result = -1
tmp = [i for i in range(m)]
for comb in combinations(tmp, 3):
    result = 0
    tmpq = copy.deepcopy(q)
    # print(comb)
    for _ in range(n):  # n턴
        kill_index = set()
        for ci in range(3):  # 궁수 셋
            x = n
            y = comb[ci]
            flag = False
            for i in range(1, d+1):
                dx = [-p for p in range(1, i+1)] + [-p for p in range(i-1, 0, -1)]
                dy = [p for p in range(-(i-1), i)]
                # print(dx, dy)
                for k in range(2*i-1):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and tmpq[nx][ny] == 1:
                        kill_index.add((nx, ny))
                        flag = True
                        break
                if flag:
                    break
            # if min_dist != 1000:
            #     kill_index.add((rx, ry))
            #     print(min_dist)

        # print(kill_index)
        # for i in range(n):
        #     print(tmpq[i])
        # print()
        for x, y in kill_index:
            tmpq[x][y] = 0
            result += 1
        tmpq.pop()
        tmpq.appendleft([0 for _ in range(m)])
    # print(result)
    max_result = max(max_result, result)

print(max_result)





# 5 5 1
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 1 1 1 1 1

# 4 4 4
# 1 1 1 0
# 1 1 1 1
# 0 0 1 0
# 0 0 1 1
