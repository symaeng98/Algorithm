from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 1:
                # 이전 값의 + 1을 넣어주는 것이 포인트
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[N-1][M-1]

print(bfs(0,0))

# cnt가 증가했다 줄어들어야 하는 것처럼 복잡하다면 cnt를 사용하는 문제가 아닐 수 있다.
# 다시 줄어든다는 것은 이전 시행과 연관이 있기 때문에 dp 느낌으로 값을 저장해 나가자