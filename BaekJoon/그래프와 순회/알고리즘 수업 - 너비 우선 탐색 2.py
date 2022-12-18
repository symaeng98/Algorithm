import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

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

def bfs(r):
    global cnt
    q = deque()
    q.append(r)
    visited[r] = cnt
    while(q):
        p = q.popleft()
        for g in graph[p]:
            if visited[g] == 0:
                cnt += 1
                visited[g] = cnt
                q.append(g)


bfs(r)

for i in range(1, n+1):
    print(visited[i])