from collections import deque

n = int(input())
k = int(input())
board = [[0]*n for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 2

l = int(input())

dx = [-1, 0, 1, 0] # 위, 오, 아래, 왼 순서
dy = [0, 1, 0, -1]
snake = deque()
snake.append((0,0))
board[0][0] = 1
direction = 1 # 오른쪽으로 시작
turn_list = []
for _ in range(l):
    x, c = input().split()
    turn_list.append((x,c))
time = 0
turn_index = 0

def change_direction(d):
    global direction
    if d == "D":
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1)
        if direction < 0:
            direction = 3

while True:
    if turn_index < len(turn_list) and time == int(turn_list[turn_index][0]):
        change_direction(turn_list[turn_index][1])
        turn_index += 1
    x, y = snake[-1]
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 0 <= nx < n and 0 <= ny < n:
        if board[nx][ny] == 1:
            print(time+1)
            break
        elif board[nx][ny] == 2:
            snake.append((nx,ny))
            board[nx][ny] = 1
        elif board[nx][ny] == 0:
            snake.append((nx,ny))
            board[nx][ny] = 1
            a, b = snake.popleft()
            board[a][b] = 0
    else:
        print(time+1)
        break
    time += 1