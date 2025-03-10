n = int(input())
m = int(input())
edges = []
parent = [i for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


edges.sort(key=lambda x: x[2])
result = 0
for a, b, c in edges:

    ap = find_parent(a)
    bp = find_parent(b)
    if ap == bp:
        continue
    union(a, b)
    result += c

print(result)





# 6
# 9
# 1 2 5
# 1 3 4
# 2 3 2
# 2 4 7
# 3 4 6
# 3 5 11
# 4 5 3
# 4 6 8
# 5 6 8