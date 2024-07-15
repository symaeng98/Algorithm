n, m, h = map(int, input().split())
graph = [[False] * n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = True

result = 4

def check():
    for k in range(n):
        now = k
        for j in range(h):
            if graph[j][now]:
                now += 1
            elif now > 0 and graph[j][now-1]:
                now -= 1
        if now != k:
            return False
    return True

def dfs(cnt, x, y):
    global result
    if check():
        result = min(result, cnt)
        return
    elif cnt == 3 or result <= cnt:
        return
    for i in range(x, h):
        if i == x:
            now = y
        else:
            now = 0
        for j in range(now, n-1):
            if not graph[i][j] and not graph[i][j+1]:
                if j > 0 and graph[i][j-1]:
                    continue
                graph[i][j] = True
                dfs(cnt + 1, i, j+2)
                graph[i][j] = False


dfs(0, 0, 0)
if result < 4:
    print(result)
else:
    print(-1)