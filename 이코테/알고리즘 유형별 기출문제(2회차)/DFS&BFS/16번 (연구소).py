from itertools import combinations

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

virus_list = []
blank_list = []
wall_list = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus_list.append((i,j))
        if board[i][j] == 0:
            blank_list.append((i,j))
        if board[i][j] == 1:
            wall_list.append((i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(v_x, v_y):
    for i in range(4):
        nx = v_x + dx[i]
        ny = v_y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                dfs(nx, ny)

max_value = 0
for comb in combinations(blank_list, 3):
    for c in comb:
        board[c[0]][c[1]] = 2
    for v_x, v_y in virus_list:
        dfs(v_x, v_y)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1
    if max_value < cnt:
        max_value = cnt

    for v in virus_list:
        i, j = v
        board[i][j] = 2
    for w in wall_list:
        i, j = w
        board[i][j] = 1
    for b in blank_list:
        i, j = b
        board[i][j] = 0

print(max_value)