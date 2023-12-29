INF = 1e9
t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    positions = [[] for _ in range(k+1)]
    for i in range(n):
        for j in range(n):
            positions[board[i][j]].append((i,j))

    flag = False
    for i in range(1, k+1):
        if len(positions[i]) == 0:
            print(f"#{test_case} {-1}")
            flag = True
            break
    if flag:
        continue

    dp = [[INF]*n for _ in range(n)]
    for x, y in positions[1]:
        dp[x][y] = 0

    now = 2
    while now <= k:
        for x, y in positions[now]:
            for b_x, b_y in positions[now-1]:
                dp[x][y] = min(dp[x][y], dp[b_x][b_y] + abs(x-b_x)+abs(y-b_y))
        now += 1

    answer = 1e9
    for k_x, k_y in positions[k]:
        answer = min(answer, dp[k_x][k_y])
    print(f"#{test_case} {answer}")
