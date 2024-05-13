from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
INF = 1e9

def bfs(i, j):
    global num
    q = deque([(i, j)])
    graph[i][j] = num
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = num
                    visited[nx][ny] = True
    

num = 1
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            num += 1


def check(k):
    distance = [[INF]*n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if graph[i][j] == k:
                distance[i][j] = 0
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] != 0 and graph[nx][ny] != k:
                    return distance[x][y]
                elif graph[nx][ny] == 0 and distance[nx][ny] == INF:
                    distance[nx][ny] = min(distance[nx][ny], distance[x][y] + 1)
                    q.append((nx, ny))

result = INF
for i in range(1, num):
    result = min(result, check(i))
print(result)