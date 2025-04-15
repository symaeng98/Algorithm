import sys

sys.setrecursionlimit(10**9)

cnt = 0
def dfs(board, start, n, visited, a):
    global cnt

    visited[start] = True
    tmp = 0
    for x in board[start]:
        if not visited[x]:
            v = dfs(board, x, n, visited, a)
            tmp += v
            cnt += abs(v)

    a[start] += tmp
    return a[start]


def solution(a, edges):
    n = len(a)
    graph = [[] for _ in range(n)]
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    visited = [False]*n
    dfs(graph, 0, n, visited, a)

    if a[0] == 0:
        return cnt
    else:
        return -1