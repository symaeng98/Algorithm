from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
component_list = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(s):
    if visited[s]:
        return
    component = [s]
    q = deque()
    q.append(s)
    visited[s] = True
    e = 0
    while q:
        s = q.popleft()
        for g in graph[s]:
            e += 1
            if visited[g]:
                continue
            q.append(g)
            visited[g] = True
            component.append(g)

    component_list.append((sorted(component), e//2))


for i in range(1, n+1):
    bfs(i)

max_component_index = 0
max_den = component_list[0][1] / len(component_list[0][0])
for i in range(1, len(component_list)):
    c_len = len(component_list[i][0])
    e = component_list[i][1]
    den = e / c_len
    if den > max_den:
        max_den = den
        max_component_index = i
    elif den == max_den:
        if len(component_list[max_component_index][0]) > len(component_list[i][0]):
            max_component_index = i
        elif len(component_list[max_component_index][0]) == len(component_list[i][0]):
            if component_list[max_component_index][0][0] > component_list[i][0][0]:
                max_component_index = i

for c in component_list[max_component_index][0]:
    print(c, end=" ")