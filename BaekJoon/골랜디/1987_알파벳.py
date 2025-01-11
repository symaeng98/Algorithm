r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

max_cnt = 0

visited = [graph[0][0]]


def dfs(cnt, x, y):
    global max_cnt
    if cnt > max_cnt:
        max_cnt = cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] not in visited:
                visited.append(graph[nx][ny])
                dfs(cnt+1, nx, ny)
                visited.pop()

dfs(1, 0, 0)

print(max_cnt)

# 5 5
# IEFCJ
# FHFKC
# FFALF
# HFGCF
# HMCHH