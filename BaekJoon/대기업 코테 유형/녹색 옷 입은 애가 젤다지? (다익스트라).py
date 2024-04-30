import heapq

INF = 1e9
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
test = 1
while True:
    n = int(input())
    if n == 0:
        break
    board = [list(map(int, input().split())) for _ in range(n)]

    distance = [[INF]*n for _ in range(n)]
    q = []
    heapq.heappush(q, (board[0][0], 0, 0))
    distance[0][0] = board[0][0]
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + board[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    print(f"Problem {test}: {distance[n-1][n-1]}")
    test += 1