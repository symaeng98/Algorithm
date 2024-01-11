r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_cnt = 0

visited = set(board[0][0])
def dfs(cnt, x, y):
    global max_cnt
    max_cnt = max(cnt, max_cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in visited:
            visited.add(board[nx][ny])
            dfs(cnt+1, nx, ny)
            visited.remove(board[nx][ny])

dfs(1, 0, 0)
print(max_cnt)
