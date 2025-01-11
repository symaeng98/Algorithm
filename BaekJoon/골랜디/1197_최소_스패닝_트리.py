def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


v, e = map(int, input().split())
edges = []
parents = [i for i in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

result = 0
for c, a, b in edges:
    ap = find_parent(a)
    bp = find_parent(b)
    if ap == bp:
        continue

    union_parent(a, b)
    result += c

print(result)

# 3 3
# 1 2 1
# 2 3 2
# 1 3 3