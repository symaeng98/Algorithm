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

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))
parent = [i for i in range(n+1)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            union_parent(parent, i+1, j+1)

plan_parent = parent[plan[0]]
flag = True
for p in plan:
    if plan_parent != parent[p]:
        print("NO")
        flag = False
        break
if flag:
    print("YES")