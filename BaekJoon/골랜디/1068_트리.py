n = int(input())
t = list(map(int, input().split()))
graph = [[] for _ in range(n)]
start = 0
x = int(input())
for i in range(n):
    if t[i] == -1:
        start = i
        continue
    graph[t[i]].append(i)

result = 0

def dfs(s):
    global result
    if s == x:
        return
    if not graph[s] or (len(graph[s]) == 1 and graph[s][0] == x):
        result += 1
        return

    for v in graph[s]:
        dfs(v)


dfs(start)
print(result)
