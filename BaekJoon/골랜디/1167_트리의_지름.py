n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    arr = list(map(int, input().split()))
    v = arr[0]
    arr = arr[1:-1]
    for j in range(len(arr)//2):
        graph[v].append((arr[2*j], arr[2*j+1]))


def dfs(s):
    distance = [-1]*(n+1)
    stack = []
    stack.append(s)
    distance[s] = 0

    while stack:
        x = stack.pop()
        for v, c in graph[x]:
            if distance[v] == -1:
                distance[v] = distance[x] + c
                stack.append(v)
    return distance

distance = dfs(1)
# print(distance)
max_v = distance.index(max(distance))

distance = dfs(max_v)
print(max(distance))

# 5
# 1 3 2 -1
# 2 4 4 -1
# 3 1 2 4 3 -1
# 4 2 4 3 3 5 6 -1
# 5 4 6 -1