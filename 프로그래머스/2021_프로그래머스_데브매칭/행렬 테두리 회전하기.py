def rotate(board, x1, y1, x2, y2):
    min_value = board[x1][y1]
    u_cnt, l_cnt = x2-x1, y2-y1

    k = board[x1][y1]
    for i in range(u_cnt):
        board[x1+i][y1] = board[x1+i+1][y1]
        min_value = min(min_value, board[x1+i+1][y1])
    for i in range(l_cnt):
        board[x2][y1+i] = board[x2][y1+i+1]
        min_value = min(min_value, board[x2][y1+i+1])
    for i in range(u_cnt):
        board[x2-i][y2] = board[x2-i-1][y2]
        min_value = min(min_value, board[x2-i-1][y2])
    for i in range(l_cnt):
        board[x1][y2-i] = board[x1][y2-i-1]
        min_value = min(min_value, board[x1][y2-i-1])
    board[x1][y1+1] = k

    return min_value


def solution(rows, columns, queries):
    board = [[0]*columns for _ in range(rows)]
    start = 1
    for i in range(rows):
        for j in range(columns):
            board[i][j] = start
            start += 1
    result = []
    for query in queries:
        result.append(rotate(board, query[0]-1, query[1]-1, query[2]-1, query[3]-1))

    return result


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100, 97, [[1,1,100,97]]))