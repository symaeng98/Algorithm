t = int(input())
for _ in range(t):
    n = int(input())
    students = list(map(int, input().split()))
    students.insert(0,0)

    visited = [False]*(n+1)

    result = 0
    def check(s):
        global result

        visited[s] = True
        tmp.append(s)
        x = students[s]
        if visited[x]:
            if x in tmp:
                result += len(tmp[tmp.index(x):])
            return
        else:
            check(x)


    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            tmp = []
            check(i)

    print(n-result)