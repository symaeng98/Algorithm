from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

result_list = []
for i in range(1, n+1):
    if visited[i]:
        continue
    q = deque()
    q.append(i)
    visited[i] = True
    uni = [i]
    while q:
        now = q.popleft()
        for g in graph[now]:
            if visited[g]:
                continue
            if now in graph[g]:
                q.append(g)
                uni.append(g)
                visited[g] = True

    result_list.append(uni)

print(len(result_list))