n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n):
    tmp = list(map(int, input().split()))
    v = tmp[0]
    info = tmp[1:-1]
    for j in range(len(info)//2):
        graph[v].append((info[j*2], info[j*2+1]))

max_value = -1
def dfs(s, p):
    global max_value
    if len(graph[s]) == 1 and graph[s][0][0] == p:
        return 0

    res = []
    for g in graph[s]:
        if g[0] == p:
            continue
        res.append(g[1] + dfs(g[0], s))

    res.sort(reverse=True)

    max_value = max(max_value, sum(res[:2]))

    return res[0]

result = []
for g in graph[1]:
    result.append(dfs(g[0], 1)+g[1])
result.sort(reverse=True)
print(max(max_value, sum(result[:2])))


# 5
# 1 3 2 -1
# 2 4 100 -1
# 3 1 2 4 3 -1
# 4 2 100 3 3 5 100 -1
# 5 4 100 -1