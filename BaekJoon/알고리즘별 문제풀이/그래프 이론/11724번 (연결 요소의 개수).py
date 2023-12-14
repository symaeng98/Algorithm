n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(s):
    if visited[s]:
        return False
    stack = []
    stack.append(s)

    while stack:
        x = stack.pop()
        if not visited[x]:
            visited[x] = True
            for g in graph[x]:
                stack.append(g)

    return True

result = 0
visited = [False]*(n+1)
for i in range(1, n+1):
    if dfs(i):
        result += 1
print(result)