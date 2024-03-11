from collections import deque

def bfs(n, graph, s):
    visited = [False]*(n+1)
    q = deque()
    q.append(s)
    visited[s] = True
    cnt = 0
    while q:
        x = q.popleft()
        for g in graph[x]:
            if not visited[g]:
                visited[g] = True
                q.append(g)
                cnt += 1
    return cnt

def solution(n, wires):
    graph = [[]*(n+1) for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    min_cnt = 100
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        a_cnt = bfs(n, graph, a)
        b_cnt = bfs(n, graph, b)

        min_cnt = min(abs(a_cnt - b_cnt), min_cnt)

        graph[a].append(b)
        graph[b].append(a)

    return min_cnt


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))