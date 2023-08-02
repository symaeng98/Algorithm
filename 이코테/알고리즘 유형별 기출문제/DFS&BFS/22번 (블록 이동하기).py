from collections import deque

def getNextPosition(pos, board):
    np = []
    pos = list(pos)
    x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx1 = x1 + dx[i]
        ny1 = y1 + dy[i]
        nx2 = x2 + dx[i]
        ny2 = y2 + dy[i]
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            np.append({(nx1, ny1), (nx2, ny2)})
    if x1 == x2:
        for i in [-1, 1]:
            if board[x1+i][y1] == 0 and board[x2+i][y2] == 0:
                np.append({(x1, y1), (x1+i, y1)})
                np.append({(x2, y2), (x2+i, y2)})
    elif y1 == y2:
        for i in [-1, 1]:
            if board[x1][y1+i] == 0 and board[x2][y2+i] == 0:
                np.append({(x1, y1), (x1, y1+i)})
                np.append({(x2, y2), (x2, y2+i)})
    return np

def solution(board):
    n = len(board)
    newBoard = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            newBoard[i+1][j+1] = board[i][j]
    q = deque()
    visited = []
    pos = {(1,1), (1,2)}
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        if (n,n) in pos:
            return cost
        for np in getNextPosition(pos, newBoard):
            if np not in visited:
                q.append((np, cost+1))
                visited.append(np)
    return 0

