import copy

tmp = [list(map(int, input().split())) for _ in range(4)]
board = [[] for _ in range(4)]
for i in range(4):
    for j in range(0,8,2):
        board[i].append([tmp[i][j], tmp[i][j+1]-1])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def turn_left(direction):
    return (direction + 1) % 8

result = 0

def find_fish(arr, index):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == index:
                return (i,j)
    return None

def move_fish(arr, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(arr, i)
        if position != None:
            x, y = position[0], position[1]
            direction = arr[x][y][1]
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == now_x and ny == now_y):
                        arr[x][y][1] = direction
                        arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
                        break
                direction = turn_left(direction)
def get_possible_positions(arr, now_x, now_y):
    positions = []
    direction = arr[now_x][now_y][1]
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        if 0 <= now_x < 4 and 0 <= now_y < 4:
            if arr[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions

def dfs(arr, now_x, now_y, total):
    global result
    arr = copy.deepcopy(arr)

    total += arr[now_x][now_y][0]
    arr[now_x][now_y][0] = -1

    move_fish(arr, now_x, now_y)

    positions = get_possible_positions(arr, now_x, now_y)

    if len(positions) == 0:
        result = max(result, total)
        return

    for next_x, next_y in positions:
        dfs(arr, next_x, next_y, total)

dfs(board, 0, 0, 0)
print(result)