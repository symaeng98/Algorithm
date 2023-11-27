edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
# edges = [[2, 3], [4, 3], [1, 1], [2, 1]]

def check_doughnut(graph, v):
    visited = []
    stack = [v]

    while stack:
        v = stack.pop()
        if len(graph[v]) != 1: # outdegree가 하나여야만 함
            return False
        for x in graph[v]:
            if x not in visited:
                visited.append(x)
                stack.append(x)
    return True


def check_stick(graph, v):
    visited = []
    stack = [v]

    while stack:
        v = stack.pop()
        if len(graph[v]) > 1: # outdegree가 하나 혹은 없어야 함
            return False
        for x in graph[v]:
            if x in visited:
                return False
            visited.append(x)
            stack.append(x)
    return True


def check_eight(graph, v):
    visited = []
    stack = [v]

    while stack:
        v = stack.pop()
        if len(graph[v]) == 2: # outdegree가 두 개인 것이 있어야 함
            return True
        for x in graph[v]:
            if x not in visited:
                visited.append(x)
                stack.append(x)
    return False


max_value = -1
for e in edges:
    max_value = max(e[0], e[1], max_value)

graph = [[] for _ in range(max_value+1)]
indegree = [0]*(max_value+1)

for e in edges:
    graph[e[0]].append(e[1])
    indegree[e[1]] += 1

for i in range(1, max_value+1):
    v_count = 0 # 정점인지 확인 용
    result = [0, 0, 0, 0]
    if indegree[i] != 0:
        continue
    for v in graph[i]:
        if check_doughnut(graph, v):
            v_count += 1
            result[1] += 1
            continue
        if check_stick(graph, v):
            v_count += 1
            result[2] += 1
            continue
        if check_eight(graph, v):
            v_count += 1
            result[3] += 1

    if v_count >= 2:
        result[0] = i
        print(result)
        break