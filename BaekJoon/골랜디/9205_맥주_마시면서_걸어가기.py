from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    conveniences = [tuple(map(int, input().split())) for _ in range(n)]
    fx, fy = map(int, input().split())

    q = deque()
    q.append((hx, hy))
    visited = []
    success = False
    while q:
        x, y = q.popleft()
        if abs(fx-x)+abs(fy-y) <= 1000:
            success = True
            break
        for cx, cy in conveniences:
            if (cx, cy) not in visited and abs(cx-x)+abs(cy-y) <= 1000:
                q.append((cx, cy))
                visited.append((cx, cy))

    if success:
        print("happy")
    else:
        print("sad")
