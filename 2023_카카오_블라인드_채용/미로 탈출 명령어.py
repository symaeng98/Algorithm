from collections import deque

def solution(n, m, x, y, r, c, k):
    q = deque([(x, y, "", 0)])
    dt = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]

    while q:
        x, y, path, cnt = q.popleft()
        if (x, y) == (r, c) and (k - cnt) % 2 == 1:
            return "impossible"
        if (x, y) == (r, c) and cnt == k:
            return path
        for i in range(4):
            dx, dy, direction = dt[i]
            nx = x + dx
            ny = y + dy
            if 0 < nx <= n and 0 < ny <= m and abs(nx - r) + abs(ny - c) <= k - (cnt + 1):
                q.append((nx, ny, path + direction, cnt + 1))
                break

    return "impossible"

print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))