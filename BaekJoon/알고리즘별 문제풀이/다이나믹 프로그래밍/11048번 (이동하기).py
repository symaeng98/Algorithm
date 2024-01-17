n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dx = [0, 1, 1]
dy = [1, 0, 1]

dp[0][0] = board[0][0]
x, y = 0, 0
for i in range(n):
    for j in range(m):
        for k in range(3):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                dp[nx][ny] = max(dp[nx][ny], dp[i][j]+board[nx][ny])

result = 0
for i in range(n):
    for j in range(m):
        result = max(result, dp[i][j])

print(result)