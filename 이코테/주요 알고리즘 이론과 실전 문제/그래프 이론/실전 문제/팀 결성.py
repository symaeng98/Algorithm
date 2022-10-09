def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(a, b, parent):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i

for i in range(m):
    a, b, c = map(int,input().split())
    if a == 0:
        union_parent(b,c,parent)
    else:
        if find_parent(parent,b) == find_parent(parent,c):
            print("YES")
        else:
            print("NO")