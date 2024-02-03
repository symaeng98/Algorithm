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
parent = [i for i in range(n+1)]
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((b, a))
arr.sort(reverse=True)

cnt = 0
for cup, x in arr:
    fp = find_parent(parent, x)
    if fp == 0:
        continue
    cnt += cup
    union_parent(parent, fp, fp-1)

print(cnt)