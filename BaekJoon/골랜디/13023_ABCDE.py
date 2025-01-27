def dfs(visited, s, cnt):
    global result
    if cnt == 4:
        result = True
        return
    for x in graph[s]:
        if not visited[x]:
            visited[x] = True
            dfs(visited, x, cnt+1)
            visited[x] = False


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
edges = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


flag = False
for i in range(n):
    visited = [False]*n
    result = False
    visited[i] = True
    dfs(visited, i, 0)
    if result:
        flag = True
        break

if flag:
    print(1)
else:
    print(0)



# 8 8
# 1 7
# 3 7
# 4 7
# 3 4
# 4 6
# 3 5
# 0 4
# 2 7