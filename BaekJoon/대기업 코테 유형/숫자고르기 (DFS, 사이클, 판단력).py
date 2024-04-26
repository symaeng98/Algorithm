n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.insert(0,0)
result = set()

def dfs(x):
    visited[x] = True
    stack = [arr[x]]

    while stack:
        v = stack.pop()
        if not visited[v]:
            stack.append(arr[v])
            visited[v] = True
        else:
            result.add(v)

for i in range(1, n+1):
    visited = [False]*(n+1)
    dfs(i)

print(len(result))
for r in sorted(list(result)):
    print(r)

