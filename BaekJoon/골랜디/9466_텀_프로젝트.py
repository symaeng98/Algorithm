def dfs(s):
    global result
    visited[s] = True
    tmp.append(s)
    x = arr[s]
    if visited[x]:
        if x in tmp:
            result += len(tmp[tmp.index(x):])
        return
    else:
        dfs(x)


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)

    visited = [False]*(n+1)

    result = 0
    for i in range(1, n+1):
        if not visited[i]:
            tmp = []
            dfs(i)
    print(n-result)