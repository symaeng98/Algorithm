from itertools import combinations

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input().split()))

x_list = []
student_list = []
teacher_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            x_list.append((i,j))
        elif graph[i][j] == 'S':
            student_list.append((i,j))
        elif graph[i][j] == 'T':
            teacher_list.append((i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(graph, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 'S':
                return False
            if graph[nx][ny] == 'O':
                break
            nx += dx[i]
            ny += dy[i]
    return True

result = False
for combs in combinations(x_list, 3):
    for c in combs:
        graph[c[0]][c[1]] = 'O'

    flag = True
    for tx, ty in teacher_list:
        dfs_result = dfs(graph, tx, ty)
        if not dfs_result:
            flag = False
            break

    for c in combs:
        graph[c[0]][c[1]] = 'X'

    if flag:
        result = True
        break

if result:
    print("YES")
else:
    print("NO")