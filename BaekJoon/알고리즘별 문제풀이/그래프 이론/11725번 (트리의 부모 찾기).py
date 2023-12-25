n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0] * (n+1)
stack = [1]
visited = []
while stack:
    x = stack.pop()
    visited.append(x)
    for child in tree[x]:
        if parents[child] == 0 and child not in visited:
            parents[child] = x
            stack.append(child)


for i in range(2, len(parents)):
    print(parents[i])