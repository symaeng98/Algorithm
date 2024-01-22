from collections import deque

def solution(board):
    INF = 1e9
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q = deque()
    n = len(board)
    m = len(board[0])
    visited = [[INF for _ in range(m)] for _ in range(n)]

    for x in range(n):
        for y in range(m):
            if board[x][y] == 'R':
                q.append((x, y))
                visited[x][y] = 0
            if board[x][y] == 'G':
                dest_x, dest_y = x, y

    while q:
        x, y = q.popleft()
        for d in directions:
            now_x, now_y = x, y
            nx = x + d[0]
            ny = y + d[1]
            while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != "D":
                now_x = nx
                now_y = ny
                nx += d[0]
                ny += d[1]

            if visited[now_x][now_y] == INF:
                q.append((now_x, now_y))
                visited[now_x][now_y] = min(visited[now_x][now_y], visited[x][y] + 1)

    if visited[dest_x][dest_y] == INF:
        return -1
    return visited[dest_x][dest_y]

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
print(solution([".D.R", "....", ".G..", "...D"]))