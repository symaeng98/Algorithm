from collections import deque

n = int(input())
m = int(input())
tmp = [list(map(int, input().split())) for _ in range(n)]
trip = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if tmp[i][j] == 1:
            graph[i+1].append(j+1)


visited = [False]*(n+1)
q = deque()
q.append(trip[0])
visited[trip[0]] = True
result = [trip[0]]
while q:
    v = q.popleft()
    for g in graph[v]:
        if not visited[g]:
            q.append(g)
            result.append(g)
            visited[g] = True

flag = True
for t in trip:
    if t not in result:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")