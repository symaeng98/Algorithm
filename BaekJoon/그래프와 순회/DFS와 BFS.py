from collections import deque
n, m, v = map(int, input().split(" "))
graph = [[] for _ in range(n+1)]
visitedDfs = [False] * (n+1)
visitedBfs = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()


def dfs(v):
    visitedDfs[v] = True
    print(v, end=" ")
    for g in graph[v]:
        if not visitedDfs[g]:
            dfs(g)


dfs(v)
print()


def bfs(v):
    q = deque()
    q.append(v)
    visitedBfs[v] = True
    while(q):
        p = q.popleft()
        print(p, end=" ")
        for g in graph[p]:
            if not visitedBfs[g]:
                visitedBfs[g] = True
                q.append(g)

bfs(v)