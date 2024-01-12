def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

result = 0
result_tree = []
parent = [i for i in range(v+1)]
for cost, v1, v2 in edges:
    x1 = find_parent(parent, v1)
    x2 = find_parent(parent, v2)
    if x1 == x2:
        continue
    union_parent(parent, x1, x2)
    result += cost

print(result)