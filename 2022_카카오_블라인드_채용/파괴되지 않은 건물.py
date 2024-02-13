def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    tmp = [[0]*(m+1) for _ in range(n+1)]
    for t, r1, c1, r2, c2, degree in skill:
        point = degree
        if t == 1:
            point *= -1
        tmp[r1][c1] += point
        tmp[r2+1][c2+1] += point
        tmp[r2+1][c1] -= point
        tmp[r1][c2+1] -= point

    for i in range(n):
        for j in range(m+1):
            tmp[i+1][j] += tmp[i][j]

    for i in range(n+1):
        for j in range(m):
            tmp[i][j+1] += tmp[i][j]

    for i in range(n):
        for j in range(m):
            board[i][j] += tmp[i][j]

    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                cnt += 1

    return cnt

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))