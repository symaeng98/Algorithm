def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
m = int(input())
arr = [int(input()) for _ in range(m)]
parent = [i for i in range(0, n+1)]

cnt = 0
for a in arr:
    x = find_parent(parent, a)
    if x == 0:
        break
    union_parent(parent, x-1, x)
    cnt += 1
print(cnt)