n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

move_arr = map(int, input().split())

def dice_move(dice, direction):
    if direction == 1:
        tmp0 = dice[0]
        tmp1 = dice[1]
        tmp2 = dice[2]
        tmp3 = dice[3]
        dice[0] = tmp3
        dice[1] = tmp2
        dice[2] = tmp0
        dice[3] = tmp1
    if direction == 2:
        tmp0 = dice[0]
        tmp1 = dice[1]
        tmp2 = dice[2]
        tmp3 = dice[3]
        dice[0] = tmp2
        dice[1] = tmp3
        dice[2] = tmp1
        dice[3] = tmp0
    if direction == 3:
        tmp0 = dice[0]
        tmp1 = dice[1]
        tmp4 = dice[4]
        tmp5 = dice[5]
        dice[0] = tmp4
        dice[1] = tmp5
        dice[4] = tmp1
        dice[5] = tmp0
    if direction == 4:
        tmp0 = dice[0]
        tmp1 = dice[1]
        tmp4 = dice[4]
        tmp5 = dice[5]
        dice[0] = tmp5
        dice[1] = tmp4
        dice[4] = tmp0
        dice[5] = tmp1


dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0] # 위, 아래, 왼, 오, 앞, 뒤
for d in move_arr:
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < m:
        dice_move(dice, d)
        if board[nx][ny] == 0: # 칸이 0이면
            board[nx][ny] = dice[1]
        else:
            dice[1] = board[nx][ny]
            board[nx][ny] = 0
        print(dice[0])
        x = nx
        y = ny
