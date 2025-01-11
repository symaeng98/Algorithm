from collections import defaultdict, deque


def bfs(graph, v):
    if set_map[v] != 0:
        return True

    q = deque()
    set_map[v] = 1
    q.append(v)

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if set_map[nx] != 0:
                if set_map[nx] == set_map[x]:
                    return False
                continue
            set_map[nx] = switch_map[set_map[x]]
            q.append(nx)
    return True


k = int(input())
switch_map = {1: 2, 2: 1}
for _ in range(k):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v+1)]
    set_map = defaultdict(int)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = "YES"
    for i in range(1, v+1):
        if bfs(graph, i):
            continue
        result = "NO"
    print(result)


# 2
# 3 2
# 1 3
# 2 3
# 4 4
# 1 2
# 2 3
# 3 4
# 4 2