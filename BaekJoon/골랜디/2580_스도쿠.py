graph = [list(map(int, input().split())) for _ in range(9)]

empty = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            empty.append((i, j))


def check(x, y, k):
    for i in range(9):
        if y == i:
            continue
        if graph[x][i] == k:
            return False

    for i in range(9):
        if x == i:
            continue
        if graph[i][y] == k:
            return False

    iter_map = [[0, 1, 2], [0, 1, 2], [0, 1, 2], [3, 4, 5], [3, 4, 5], [3, 4, 5], [6, 7, 8], [6, 7, 8], [6, 7, 8]]
    for i in iter_map[x]:
        for j in iter_map[y]:
            if i == x and j == y:
                continue
            if graph[i][j] == k:
                return False
    return True

flag = False
def dfs(index):
    global flag
    if flag:
        return
    if index == len(empty):
        for i in range(9):
            for j in range(9):
                print(graph[i][j], end=" ")
            print()
        flag = True
        return
    for i in range(len(empty)):
        if i != index:
            continue
        x, y = empty[index]
        if graph[x][y] != 0:
            continue
        for k in range(1, 10):
            if check(x, y, k):
                graph[x][y] = k
                dfs(index+1)
                graph[x][y] = 0


dfs(0)

# 0 3 5 4 6 9 2 7 8
# 7 8 2 1 0 5 6 0 9
# 0 6 0 2 7 8 1 3 5
# 3 2 1 0 4 6 8 9 7
# 8 0 4 9 1 3 5 0 6
# 5 9 6 8 2 0 4 1 3
# 9 1 7 6 5 2 0 8 0
# 6 0 3 7 0 1 9 5 2
# 2 5 8 3 9 4 7 6 0