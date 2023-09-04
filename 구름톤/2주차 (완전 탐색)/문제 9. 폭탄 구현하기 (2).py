n, k = map(int, input().split())

boardStr = [list(input().split()) for _ in range(n)]
board = [[0 for _ in range(n)]for _ in range (n)]

doubleBombList = []

for i in range(n):
    for j in range(n):
        if boardStr[i][j] == "@":
            boardStr[i][j] = "-2"
        elif boardStr[i][j] == "#":
            boardStr[i][j] = "-1"

for i in range(n):
    for j in range(n):
        board[i][j] = int(boardStr[i][j])

dx = [-1, 1, 0, 0, 0]
dy = [0, 0, -1, 1, 0]

for _ in range(k):
    x, y = map(int, input().split())
    for i in range(5):
        nx = (x-1) + dx[i]
        ny = (y-1) + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == -1:
                continue
            if board[nx][ny] < 0:
                board[nx][ny] -= 2
            else:
                board[nx][ny] += 1


result = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == -1:
            continue
        elif board[i][j] < 0:
            board[i][j] = -board[i][j] - 2
        result = max(result, int(board[i][j]))
print(result)