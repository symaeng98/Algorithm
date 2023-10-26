import sys, copy
input = sys.stdin.readline
n = int(input())
ans = 0

graph = [list(map(int, input().split())) for _ in range(n)]

def left(board):
    for i in range(n):
        index = 0
        for j in range(1, n):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][index] == 0:
                    board[i][index] = tmp

                elif board[i][index] == tmp:
                    board[i][index] *= 2
                    index += 1
                else:
                    index += 1
                    board[i][index] = tmp

    return board

def right(board):
    for i in range(n):
        index = n - 1
        for j in range(n - 2, -1, -1):

            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][index] == 0:
                    board[i][index] = tmp

                elif board[i][index] == tmp:
                    board[i][index] *= 2
                    index -= 1
                else:
                    index -= 1
                    board[i][index] = tmp
    return board

def up(board):
    for j in range(n):
        index = 0
        for i in range(n):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[index][j] == 0:
                    board[index][j] = tmp

                elif board[index][j] == tmp:
                    board[index][j] *= 2
                    index += 1

                else:
                    index += 1
                    board[index][j] = tmp
    return board

def down(board):
    for j in range(n):
        index = n - 1
        for i in range(n - 2, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[index][j] == 0:
                    board[index][j] = tmp

                elif board[index][j] == tmp:
                    board[index][j] *= 2
                    index -= 1

                else:
                    index -= 1
                    board[index][j] = tmp
    return board

def dfs(cnt, arr):
    global ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                if arr[i][j] > ans:
                    ans = arr[i][j]
        return

    for i in range(4):
        copy_arr = copy.deepcopy(arr)
        if i == 0:
            dfs(cnt + 1, left(copy_arr))
        elif i == 1:
            dfs(cnt + 1, right(copy_arr))
        elif i == 2:
            dfs(cnt + 1, up(copy_arr))
        else:
            dfs(cnt + 1, down(copy_arr))

dfs(0, graph)
print(ans)