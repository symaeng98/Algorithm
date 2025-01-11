from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
distance_graph = [[[0]*m for _ in range(n)] for _ in range(2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0, 0, 0))
distance_graph[0][0][0] = 1

def bfs():
    while q:
        x, y, wb = q.popleft()
        if x == n-1 and y == m-1:
            return distance_graph[wb][x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and distance_graph[wb][nx][ny] == 0:
                    q.append((nx, ny, wb))
                    distance_graph[wb][nx][ny] = distance_graph[wb][x][y]+1
                elif graph[nx][ny] == 1 and wb == 0:
                    q.append((nx, ny, 1))
                    distance_graph[1][nx][ny] = distance_graph[wb][x][y]+1

    return -1

print(bfs())

# 6 4
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000