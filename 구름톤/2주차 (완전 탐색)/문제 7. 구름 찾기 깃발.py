n, k = map(int, input().split())

board = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = -1 # 구름을 편의상 -1로 변경

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def find_cloud_num(x, y):
    cnt = 0
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == -1: # 구름이면
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if board[i][j] == -1:
            continue
        board[i][j] = find_cloud_num(i,j)

result = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == k:
            result += 1
print(result)