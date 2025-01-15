n, m, h = map(int, input().split())
graph = [[False] * (n+1) for _ in range(h+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True


def check():
    for j in range(1, n+1):
        now = j
        for i in range(1, h+1):
            if graph[i][now]:
                now += 1
                continue
            if now > 0 and graph[i][now-1]:
                now -= 1
        if now != j:
            return False
    return True

result = 4
def dfs(cnt, x):
    global result
    if check():
        result = min(result, cnt)
        return
    if cnt == 3:
        return
    for i in range(x, h+1):
        for j in range(1, n):
            if (not graph[i][j]) and (not graph[i][j-1]):
                graph[i][j] = True
                dfs(cnt+1, i)
                graph[i][j] = False

dfs(0, 1)
if result < 4:
    print(result)
else:
    print(-1)



# 5 5 6
# 1 1
# 3 2
# 2 3
# 5 1
# 5 4