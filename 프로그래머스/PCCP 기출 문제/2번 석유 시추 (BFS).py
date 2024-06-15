from collections import deque, defaultdict

def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                land[i][j] = -1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    def bfs(x, y):
        q = deque([(x, y)])
        visited[x][y] = True
        land[x][y] = now
        size = 1

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if land[nx][ny] == -1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        land[nx][ny] = now
                        size += 1

        size_dict[now] = size

    visited = [[False]*m for _ in range(n)]
    size_dict = defaultdict(int)
    now = 1
    for i in range(n):
        for j in range(m):
            if land[i][j] != 0 and not visited[i][j]:
                bfs(i, j)
                now += 1

    max_result = -1
    for j in range(m):
        included = []
        result = 0
        for i in range(n):
            if land[i][j] != 0 and land[i][j] not in included:
                result += size_dict[land[i][j]]
                included.append(land[i][j])

        max_result = max(max_result, result)

    return max_result