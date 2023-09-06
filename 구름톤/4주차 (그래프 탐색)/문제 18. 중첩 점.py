n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]

v_arr = []

for _ in range(m):
    x, y, d = input().split()
    nx, ny = int(x)-1, int(y)-1
    if d == 'R':
        for i in range(ny,n):
            graph[nx][i] += 1
    elif d == 'L':
        for i in range(ny,-1,-1):
            graph[nx][i] += 1
    else:
        v_arr.append((nx,ny,d))


result = 0
for v in v_arr:
    nx, ny, d = v
    if d == 'D':
        for i in range(nx, n):
            result += graph[i][ny]
    elif d == 'U':
        for i in range(nx, -1, -1):
            result += graph[i][ny]

print(result)