from collections import deque

n, k, q = map(int, input().split())
graph = [list(' '.join(input()).split()) for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def add_or_remove(x,y,c):
    graph[x][y] = c

    visited = [[False]*n for _ in range(n)]
    cnt = 1
    loc_list = []
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    loc_list.append((x,y))
    while q:
        px, py = q.popleft()
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] != c or visited[nx][ny]:
                    continue
                cnt += 1
                q.append((nx, ny))
                loc_list.append((nx, ny))
                visited[nx][ny] = True

    if cnt >= k:
        for lx, ly in loc_list:
            graph[lx][ly] = '.'

for i in range(q):
    x, y, w = input().split()
    ix = int(x)-1
    iy = int(y)-1
    add_or_remove(ix, iy, w)

for i in range(n):
    for j in range(n):
        print(graph[i][j],end="")
    print()