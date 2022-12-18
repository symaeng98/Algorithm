n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for i in range(m):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()


def dfs(v):
    global cnt
    visited[v] = True
    for g in graph[v]:
        if not visited[g]:
            cnt += 1
            dfs(g)

dfs(1)
print(cnt)