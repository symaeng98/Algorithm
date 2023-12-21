def dfs(x, y, cnt):
    if arr[x][y] != 1:
        return False

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [0, -1, 1, 1, -1, 0, -1, 1]
    stack = [(x, y)]
    visited = []

    while stack:
        x, y = stack.pop()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
                if (nx, ny) not in visited:
                    stack.append((nx, ny))
                    visited.append((nx, ny))
                    arr[nx][ny] = cnt

    return True

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]

    cnt = 2
    for i in range(h):
        for j in range(w):
            if dfs(i, j, cnt):
                cnt += 1

    print(cnt-2)