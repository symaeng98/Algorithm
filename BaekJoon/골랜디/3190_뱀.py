from collections import deque, defaultdict

n = int(input())
k = int(input())
graph = [[0]*n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
l = int(input())
dir_change = defaultdict(str)
for _ in range(l):
    x, c = input().split()
    if c == "D":
        c = "R"
    dir_change[int(x)] = c

dx_dy_map = {
    "R": [0, 1],
    "D": [1, 0],
    "L": [0, -1],
    "U": [-1, 0]
}
direction_map = {
    "R": {
        "R": "D",
        "L": "U",
    },
    "D": {
        "R": "L",
        "L": "R",
    },
    "L": {
        "R": "U",
        "L": "D",
    },
    "U": {
        "R": "R",
        "L": "L",
    }
}

snake = deque()
snake.append((0, 0))
direction = "R"
now = 0
while True:
    now += 1
    dx, dy = dx_dy_map[direction]
    x, y = snake[0]
    nx = x + dx
    ny = y + dy
    if not (0 <= nx < n and 0 <= ny < n) or (nx, ny) in snake:
        break
    snake.appendleft((nx, ny))
    if graph[nx][ny] == 0:
        snake.pop()
    else:
        graph[nx][ny] = 0

    if dir_change[now]:
        direction = direction_map[direction][dir_change[now]]
    # print("시간:", now)

print(now)


# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D