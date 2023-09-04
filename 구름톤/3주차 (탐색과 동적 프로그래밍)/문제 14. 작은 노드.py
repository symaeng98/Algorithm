n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

now = k
cnt = 0
while True:
    if visited[now]:
        break
    visited[now] = True
    cnt += 1
    for g in graph[now]:
        if visited[g]:
            continue
        else:
            now = g
            break

print(cnt, now)