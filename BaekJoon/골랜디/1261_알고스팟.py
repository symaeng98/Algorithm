import heapq

m, n = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False]*m for _ in range(n)]
q = []
heapq.heappush(q, (0, 0, 0))
visited[0][0] = True
while q:
    cnt, x, y = heapq.heappop(q)
    if x == n-1 and y == m-1:
        print(cnt)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            if graph[nx][ny] == 0:
                heapq.heappush(q, (cnt, nx, ny))
            else:
                heapq.heappush(q, (cnt+1, nx, ny))
