n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
now_dir = list(map(int, input().split()))

smell = [[[0,0]]*n for _ in range(n)]

priority = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priority[i].append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if board[i][j] != 0:
                smell[i][j] = [board[i][j], k]

def move():
    new_board = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                found = False
                direction = now_dir[board[i][j] - 1]
                for l in range(4):
                    nx = i + dx[priority[board[i][j]-1][direction-1][l]-1]
                    ny = j + dy[priority[board[i][j]-1][direction-1][l]-1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0:
                            now_dir[board[i][j]-1] = priority[board[i][j]-1][direction-1][l]
                            if new_board[nx][ny] == 0:
                                new_board[nx][ny] = board[i][j]
                            else:
                                new_board[nx][ny] = min(board[i][j], new_board[nx][ny])
                            found = True
                            break
                if found:
                    continue
                for l in range(4):
                    nx = i + dx[priority[board[i][j]-1][direction-1][l]-1]
                    ny = j + dy[priority[board[i][j]-1][direction-1][l]-1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == board[i][j]:
                            now_dir[board[i][j]-1] = priority[board[i][j]-1][direction-1][l]
                            new_board[nx][ny] = board[i][j]
                            break
    return new_board

time = 0
while True:
    update_smell()
    new_board = move()
    board = new_board
    time += 1

    check = True
    for i in range(n):
        for j in range(n):
            if board[i][j] > 1:
                check = False

    if check:
        print(time)
        break

    if time >= 1000:
        print(-1)
        break
