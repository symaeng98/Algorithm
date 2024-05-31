import heapq

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
def solution(board):
    n = len(board)
    answer = 0
    result = 1e9
    distance = [[[1e9]*4 for _ in range(n)] for _ in range(n)]
    q = []
    distance[0][0][0] = 0
    distance[0][0][1] = 0
    distance[0][0][2] = 0
    distance[0][0][3] = 0

    if board[1][0] == 0:
        heapq.heappush(q, (100, 1, 0, 0))
        distance[1][0][0] = 100
    if board[0][1] == 0:
        heapq.heappush(q, (100, 0, 1, 3))
        distance[0][1][3] = 100

    while q:
        price, x, y, direction = heapq.heappop(q)

        if price > distance[x][y][direction]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                if i == direction:
                    cost = distance[x][y][direction] + 100
                    if cost <= distance[nx][ny][i]:
                        heapq.heappush(q, (cost, nx, ny, i))
                        distance[nx][ny][i] = cost
                else:
                    cost = distance[x][y][direction] + 600
                    if cost <= distance[nx][ny][i]:
                        heapq.heappush(q, (cost, nx, ny, i))
                        distance[nx][ny][i] = cost

    return min(distance[n-1][n-1])