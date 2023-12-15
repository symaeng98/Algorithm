r, c = map(int, input().split())

board = [list(input()) for _ in range(r)]
visited = [[False]*c for _ in range(r)]

dx = [-1, 0, 1]
dy = [1, 1, 1]

def dfs(x, y):
    if y == c-1:
        return True
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if board[nx][ny] != "x" and not visited[nx][ny]:
                visited[nx][ny] = True
                if dfs(nx, ny):
                    return True

    return False

result = 0
for i in range(r):
    if dfs(i, 0):
        result += 1

print(result)
