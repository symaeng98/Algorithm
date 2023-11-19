import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(r):
    global cnt
    visited[r] = cnt
    for g in graph[r]:
        if visited[g] == 0:
            cnt += 1
            dfs(g)


n, m, r = map(int, input().split(" "))
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for i in range(m):
    u, v = map(int, input().split(" "))
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort(reverse=True)

dfs(r)

for i in range(1, n+1):
    print(visited[i])