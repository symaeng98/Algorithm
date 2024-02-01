def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
arr = []
parent = [i for i in range(10001)]

for _ in range(n):
    p, d = map(int, input().split())
    arr.append((p, d))
arr.sort(key=lambda x:x[0],reverse=True)

result = 0
for p, d in arr:
    fp = find_parent(parent, d)
    if fp == 0:
        continue
    result += p
    union(parent, fp-1, fp)

print(result)