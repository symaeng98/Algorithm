from collections import deque

n, m = map(int, input().split())
in_degree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    in_degree[b] += 1
    graph[a].append(b)


q = deque()
for i in range(1, n+1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    v = q.popleft()
    print(v, end=" ")
    for x in graph[v]:
        in_degree[x] -= 1
        if in_degree[x] == 0:
            q.append(x)

# print(in_degree)

