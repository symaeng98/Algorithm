from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

num_dic = {}

def bfs(c, x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == c and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
    if cnt >= k:
        p = num_dic.get(c, 0)
        num_dic[c] = p+1

for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        bfs(graph[i][j], i, j)

sorted_num_dic = sorted(num_dic.items(), key= lambda x : (x[1], x[0]), reverse = True)
print(sorted_num_dic[0][0])