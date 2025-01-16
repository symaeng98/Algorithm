from collections import deque


def find_fish(sx, sy):
    q = deque()
    q.append((sx, sy, 0))
    graph[sx][sy] = 0
    visited = [[False]*n for _ in range(n)]
    visited[sx][sy] = True
    result = []
    while q:
        x, y, distance = q.popleft()
        if graph[x][y] != 0 and graph[x][y] < size:
            result.append((distance, x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] <= size:
                    # print(nx, ny)
                    visited[nx][ny] = True
                    q.append((nx, ny, distance+1))

    if result:
        s_r = sorted(result, key=lambda x:(x[0], x[1], x[2]))
        dist, tx, ty = s_r[0]
        graph[tx][ty] = 0
        return (tx, ty, dist)
    else:
        return (-1, -1, -1)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
shark_x, shark_y = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j

size = 2
size_cnt = 0
result = 0
tx, ty = 0, 0
while True:
    tx, ty, move_cnt = find_fish(shark_x, shark_y)
    if tx == -1 and ty == -1:
        break
    # print("잡을 물고기 위치:", tx, ty)

    # move_cnt = move(shark_x, shark_y, tx, ty)
    if move_cnt == -1:
        break
    shark_x, shark_y = tx, ty
    result += move_cnt
    # print("이동 완료. 이번 이동 거리:", move_cnt)
    # print("현재 총 이동 거리:", result)
    # print("현재 상어 위치", shark_x, shark_y)
    size_cnt += 1
    if size_cnt == size:
        size_cnt = 0
        size += 1
        # print("상어 크기 증가", size)


print(result)

# 4
# 4 3 2 1
# 0 0 0 0
# 0 0 9 0
# 1 2 3 4