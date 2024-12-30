import copy

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


def left(tmp):
    for i in range(n):
        index = 0
        for j in range(1, n):
            if tmp[i][j] != 0:
                now = tmp[i][j]
                tmp[i][j] = 0

                if tmp[i][index] == 0:
                    tmp[i][index] = now
                elif tmp[i][index] == now:
                    tmp[i][index] *= 2
                    index += 1
                elif tmp[i][index] != now:
                    index += 1
                    tmp[i][index] = now

    return tmp


def right(tmp):
    for i in range(n):
        index = n-1
        for j in range(n-2, -1, -1):
            if tmp[i][j] != 0:
                now = tmp[i][j]
                tmp[i][j] = 0

                if tmp[i][index] == 0:
                    tmp[i][index] = now
                elif tmp[i][index] == now:
                    tmp[i][index] *= 2
                    index -= 1
                elif tmp[i][index] != now:
                    index -= 1
                    tmp[i][index] = now

    return tmp


def up(tmp):
    for i in range(n):
        index = 0
        for j in range(1, n):
            if tmp[j][i] != 0:
                now = tmp[j][i]
                tmp[j][i] = 0

                if tmp[index][i] == 0:
                    tmp[index][i] = now
                elif tmp[index][i] == now:
                    tmp[index][i] *= 2
                    index += 1
                elif tmp[index][i] != now:
                    index += 1
                    tmp[index][i] = now

    return tmp


def down(tmp):
    for i in range(n):
        index = n-1
        for j in range(n-2, -1, -1):
            if tmp[j][i] != 0:
                now = tmp[j][i]
                tmp[j][i] = 0

                if tmp[index][i] == 0:
                    tmp[index][i] = now
                elif tmp[index][i] == now:
                    tmp[index][i] *= 2
                    index -= 1
                elif tmp[index][i] != now:
                    index -= 1
                    tmp[index][i] = now

    return tmp


max_cnt = 0
def dfs(cnt, board):
    global max_cnt
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                max_cnt = max(max_cnt, board[i][j])
        return

    tmp = copy.deepcopy(board)
    dfs(cnt+1, left(tmp))

    tmp = copy.deepcopy(board)
    dfs(cnt+1, right(tmp))

    tmp = copy.deepcopy(board)
    dfs(cnt+1, up(tmp))

    tmp = copy.deepcopy(board)
    dfs(cnt+1, down(tmp))


dfs(0, graph)
print(max_cnt)
# 3
# 2 2 2
# 4 4 4
# 8 8 8