from itertools import combinations
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

safe = []
wall = []
virus = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            safe.append((i,j))
        if board[i][j] == 1:
            wall.append((i,j))
        if board[i][j] == 2:
            virus.append((i,j))


def move(board, i, j):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for c in range(4):
        if i+dx[c] < 0 or i+dx[c] >= N or j+dy[c] < 0 or j+dy[c] >= M:
            continue
        if board[i+dx[c]][j+dy[c]] == 2 or board[i+dx[c]][j+dy[c]] == 1:
            continue
        if board[i+dx[c]][j+dy[c]] == 0: # 안전
            board[i+dx[c]][j+dy[c]] = 2
            move(board, i+dx[c], j+dy[c])

result = -1
for coms in combinations(safe, 3):
    # 벽 세우기
    for com in coms:
        board[com[0]][com[1]] = 1
    for v in virus:
        move(board, v[0], v[1])
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt += 1
    result = max(result, cnt)

    # 초기화
    for w in wall:
        board[w[0]][w[1]] = 1
    for v in virus:
        board[v[0]][v[1]] = 2
    for s in safe:
        board[s[0]][s[1]] = 0
print(result)

# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0


# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2