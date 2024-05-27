from collections import deque

def solution(places):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = 5
    m = 5
    def bfs(x, y):
        q = deque([(x, y, 0)])
        visited = [(x, y)]

        while q:
            x, y, cnt = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and room[nx][ny] != "X":
                    if room[nx][ny] == "P":
                        if cnt+1 <= 2:
                            return False
                    q.append((nx, ny, cnt+1))
                    visited.append((nx, ny))

        return True
    result = []
    for place in places:
        room = []
        locations = []
        for p in place:
            room.append(list(p))

        for i in range(n):
            for j in range(m):
                if room[i][j] == "P":
                    locations.append((i, j))

        is_valid = 1
        for i, j in locations:
            if not bfs(i, j):
                is_valid = 0
                break

        result.append(is_valid)

    return result