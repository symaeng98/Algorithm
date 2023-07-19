from itertools import combinations as com

def calculate(c, houseList):
    distance = 0
    for hl in houseList:
        distance += minDistance(hl, c)
    return distance

def minDistance(hl, c):
    min = 10000000
    for cl in c:
        length = abs(cl[0] - hl[0]) + abs(cl[1] - hl[1])
        if min > length:
            min = length
    return min

N, M = map(int, input().split())
board = [[x for x in map(int, input().split())] for _ in range(N)]
houseList = []
chickenList = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            houseList.append((i,j))
        elif board[i][j] == 2:
            chickenList.append((i,j))

min = 10000000
for c in com(chickenList, M):
    sum = calculate(c, houseList)
    if sum < min:
        min = sum
print(min)


# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2

# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2

# 5 1
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0