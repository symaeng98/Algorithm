N, M = map(int, input().split(" "))
A, B, d = map(int, input().split(" "))
game = []
for i in range(N):
    game.append(list(map(int, input().split(" "))))

move = [(-1,0), (0,1), (1,0), (0,-1)]

dirState = d
rowState = A
colState = B
game[A][B] = 2 #갔던 곳
cnt = 1
while True:
    noMove = 1
    for i in range(1,5): #북 서 남 동 확인
        dirState = (dirState - i + 4) % 4
        moveTo = move[dirState]
        row = rowState + moveTo[0]
        col = colState + moveTo[1]
        if game[row][col] == 0: #이동
            cnt += 1
            rowState = row
            colState = col
            noMove = 0
            game[row][col] = 2

    if noMove:
        if dirState == 0:
            reverseDirState = 2
        elif dirState == 1:
            reverseDirState = 3
        elif dirState == 2:
            reverseDirState = 0
        else:
            reverseDirState = 1
        direction = move[reverseDirState]
        row = rowState + direction[0]
        col = colState + direction[1]
        if game[row][col] == 1: #뒤 쪽이 바다면
            break
        else:
            rowState = row
            colState = col

print(cnt)