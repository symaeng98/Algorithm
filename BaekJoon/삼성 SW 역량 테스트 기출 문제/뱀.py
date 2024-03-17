from collections import deque

n = int(input())
board = [[0]*n for _ in range(n)]
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1
l = int(input())
directions = [tuple(input().split()) for _ in range(l)]

snake = deque()
snake.append((0,0))

dx, dy = 0, 1
time = 0
while True:
    for t, d in directions:
        if time == int(t):
            if dx == 0 and dy == 1:
                if d == "L":
                    dx, dy = -1, 0
                else:
                    dx, dy = 1, 0
            elif dx == 1 and dy == 0:
                if d == "L":
                    dx, dy = 0, 1
                else:
                    dx, dy = 0, -1
            elif dx == -1 and dy == 0:
                if d == "L":
                    dx, dy = 0, -1
                else:
                    dx, dy = 0, 1
            elif dx == 0 and dy == -1:
                if d == "L":
                    dx, dy = 1, 0
                else:
                    dx, dy = -1, 0
            break

    nx = snake[-1][0] + dx
    ny = snake[-1][1] + dy
    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in snake:
        snake.append((nx, ny))
        if board[nx][ny] == 0:
            snake.popleft()
        else:
            board[nx][ny] = 0
    else:
        print(time+1)
        break

    time += 1