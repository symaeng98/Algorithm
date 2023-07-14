N = int(input())
K = int(input())
direction = "E"
snakeList = [(0,0)]
board = [[0]*N for _ in range(N)]
for i in range(K):
    x, y = map(int, input().split(" "))
    board[x-1][y-1] = 2
L = int(input())
turnDict = {}
for i in range(L):
    X, C = input().split(" ")
    turnDict[int(X)] = C

def move(direction, board, hx, hy, snakeList):
    lengthLimit = N
    if direction == "E":
        if hy+1 >= lengthLimit:
            return False
        if board[hx][hy+1] == 1: # 자기 자신임
            return False

        if board[hx][hy+1] == 0: # 아무것도 없음
            board[hx][hy+1] = 1 # 이동
            snakeList.append((hx,hy+1))
            x, y = snakeList.pop(0) # 꼬리 자름
            board[x][y] = 0
            return True

        if board[hx][hy+1] == 2: # 사과임
            board[hx][hy+1] = 1 # 사과 먹고 이동
            snakeList.append((hx,hy+1))
            return True
    elif direction == "W":
        if hy-1 < 0:
            return False
        if board[hx][hy-1] == 1: # 자기 자신임
            return False

        if board[hx][hy-1] == 0: # 아무것도 없음
            board[hx][hy-1] = 1 # 이동
            snakeList.append((hx,hy-1))
            x, y = snakeList.pop(0) # 꼬리 자름
            board[x][y] = 0
            return True

        if board[hx][hy-1] == 2: # 사과임
            board[hx][hy-1] = 1 # 사과 먹고 이동
            snakeList.append((hx,hy-1))
            return True

    elif direction == "S":
        if hx+1 >= lengthLimit:
            return False
        if board[hx+1][hy] == 1: # 자기 자신임
            return False

        if board[hx+1][hy] == 0: # 아무것도 없음
            board[hx+1][hy] = 1 # 이동
            snakeList.append((hx+1,hy))
            x, y = snakeList.pop(0) # 꼬리 자름
            board[x][y] = 0
            return True

        if board[hx+1][hy] == 2: # 사과임
            board[hx+1][hy] = 1 # 사과 먹고 이동
            snakeList.append((hx+1,hy))
            return True
    else:
        if hx-1 < 0:
            return False
        if board[hx-1][hy] == 1: # 자기 자신임
            return False

        if board[hx-1][hy] == 0: # 아무것도 없음
            board[hx-1][hy] = 1 # 이동
            snakeList.append((hx-1,hy))
            x, y = snakeList.pop(0) # 꼬리 자름
            board[x][y] = 0
            return True

        if board[hx-1][hy] == 2: # 사과임
            board[hx-1][hy] = 1 # 사과 먹고 이동
            snakeList.append((hx-1,hy))
            return True


def turn(d):
    global direction
    if d == "L":
        if direction == "E":
            direction = "N"
        elif direction == "N":
            direction = "W"
        elif direction == "W":
            direction = "S"
        else:
            direction = "E"
        return
    if d == "D":
        if direction == "E":
            direction = "S"
        elif direction == "S":
            direction = "W"
        elif direction == "W":
            direction = "N"
        else:
            direction = "E"
        return


## main
for time in range(0, 10001):
    hx, hy = snakeList[-1]
    if turnDict.get(time):
        turn(turnDict[time])
    if not move(direction, board, hx, hy, snakeList):
        print(time+1)
        break
