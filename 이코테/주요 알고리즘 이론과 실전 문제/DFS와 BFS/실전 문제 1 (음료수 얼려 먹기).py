N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input())))

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x+1,y)
        return True
    else:
        return False


cnt = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            cnt += 1

print(cnt)