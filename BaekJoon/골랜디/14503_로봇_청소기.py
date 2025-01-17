n, m = map(int, input().split())
r, c, d = map(int, input().split())  # 북동남서
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
while True:
    if graph[r][c] == 0:
        graph[r][c] = 2
        result += 1

    possible = False
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                possible = True

    if possible:
        for i in range(3, -1, -1):
            k = (d+i) % 4
            nx = r + dx[k]
            ny = c + dy[k]
            flag = False
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    r, c = nx, ny
                    d = k
                    flag = True
            if flag:
                break

    else:
        nx = r + (-dx[d])
        ny = c + (-dy[d])
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 2:
                r, c = nx, ny
                continue
        break

print(result)


# 3 3
# 1 1 0
# 1 1 1
# 1 0 1
# 1 1 1