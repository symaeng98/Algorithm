n, m, x, y, k = map(int, input().split())
dice = [0, 0, 0, 0, 0, 0]
roll = [[],
        [5, 4, 2, 3, 0, 1],
        [4, 5, 2, 3, 1, 0],
        [3, 2, 0, 1, 4, 5],
        [2, 3, 1, 0, 4, 5]
        ]
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


graph = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
for c in command:
    nx = x + dx[c]
    ny = y + dy[c]
    if 0 <= nx < n and 0 <= ny < m:
        change_list = []
        for i in range(6):
            if i == roll[c][i]:
                continue
            change_list.append((i, dice[roll[c][i]]))  # i면 dice를 roll[c][i]면 dice로 변경한다
        for i, d in change_list:
            dice[i] = d

        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[1]
        else:
            dice[1] = graph[nx][ny]
            graph[nx][ny] = 0
        # print(dice)
        x = nx
        y = ny
        print(dice[0])




# 3 3 1 1 9
# 1 2 3
# 4 0 5
# 6 7 8
# 1 3 2 2 4 4 1 1 3