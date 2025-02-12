n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
plans = list(map(int, input().split()))
visited = [False]*n

result = []
def dfs(s):
    global result
    visited[s] = True
    result.append(s+1)
    for v, valid in enumerate(graph[s]):
        if valid == 1:
            if not visited[v]:
                dfs(v)


dfs(plans[0]-1)

flag = True
for v in plans:
    if v not in result:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")