dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
def search(processor, core, now, n, result, core_num):
    if now == len(core):
        lines = 0
        for i in range(n):
            for j in range(n):
                if processor[i][j] == 2:
                    lines += 1
        result.append((core_num, lines))
        return
    x, y = core[now]
    for i in range(4):
        flag = False
        nx = x + dx[i]
        ny = y + dy[i]
        # 그리기
        while 0 <= nx < n and 0 <= ny < n:
            if processor[nx][ny] != 0:
                flag = True
                break
            processor[nx][ny] = 2
            nx = nx + dx[i]
            ny = ny + dy[i]

        # 체크
        if not flag:
            search(processor, core, now+1, n, result, core_num+1)

        # 빼기
        nx = nx - dx[i]
        ny = ny - dy[i]
        while not (nx == x and ny == y):
            processor[nx][ny] = 0
            nx = nx - dx[i]
            ny = ny - dy[i]

    search(processor, core, now+1, n, result, core_num)

t = int(input())

for i in range(1, t+1):
    n = int(input())
    processor = [list(map(int, input().split())) for _ in range(n)]
    core = []
    result = []
    core_num = 0
    for j in range(n):
        for k in range(n):
            if processor[j][k] == 1:
                if j==0 or k==0 or j==n-1 or k==n-1:
                    core_num += 1
                    continue
                core.append((j, k))
    search(processor, core, 0, n, result, core_num)

    sorted_result = sorted(result, key=lambda x:(-x[0],x[1]))

    print(f"#{i} {sorted_result[0][1]}")