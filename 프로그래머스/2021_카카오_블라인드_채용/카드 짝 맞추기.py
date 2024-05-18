def solution(board, r, c):
    answer = 0
    pair = [[] for _ in range(7)]
    for k in range(1, 7):
        for i in range(4):
            for j in range(4):
                if board[i][j] == k:
                    pair[k].append((i, j))

    def is_finished():
        for i in range(4):
            for j in range(4):
                if board[i][j] != 0:
                    return False
        return True

    def nearest_position(x, y):

        distance = [[0]*4 for _ in range(4)]
        distance[x][y] = 0
        for i in range(4):
            for j in range(4):
                distance[i][j] = abs(i-x) + abs(j-y)

        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if board[i][k] != 0 or k == 0 or k == 3:
                        distance[i][k] = min(distance[i][k], distance[i][j]+1)
                for k in range(4):
                    if board[k][j] != 0 or k == 0 or k == 3:
                        distance[k][j] = min(distance[k][j], distance[i][j]+1)


        for k in range(4):
            for i in range(4):
                for j in range(4):
                    if distance[i][j] == k and board[i][j] != 0:
                        return (k, i, j)

    def to_pair(x, y, tx, ty):

        distance = [[0]*4 for _ in range(4)]
        distance[x][y] = 0
        for i in range(4):
            for j in range(4):
                distance[i][j] = abs(i-x) + abs(j-y)

        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if board[i][k] != 0 or k == 0 or k == 3:
                        distance[i][k] = min(distance[i][k], distance[i][j]+1)
                for k in range(4):
                    if board[k][j] != 0 or k == 0 or k == 3:
                        distance[k][j] = min(distance[k][j], distance[i][j]+1)


        return distance[tx][ty]

    result = 0
    while not is_finished():
        cost, i, j = nearest_position(r, c)
        result += cost
        result += 1

        for x, y in pair[board[i][j]]:
            if x != i and y != j:
                r, c = x, y
                break
        board[i][j] = 0
        # print(i, j, r, c)
        pair_cost = to_pair(i, j, r, c)
        result += pair_cost
        result += 1
        board[r][c] = 0

        # print(cost, i, j, r, c, result)

    return result