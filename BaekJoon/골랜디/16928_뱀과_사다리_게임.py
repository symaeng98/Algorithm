from collections import deque

n, m = map(int,input().split())
road = []
for _ in range(n):
    f, t = map(int, input().split())
    road.append((f, t))
for _ in range(m):
    f, t = map(int, input().split())
    road.append((f, t))

visited = [False]*101
q = deque()
q.append((1, 0))
visited[1] = True
while q:
    x, cnt = q.popleft()
    # print(x, cnt)
    if x == 100:
        print(cnt)
        break

    for i in range(1, 7):
        nx = x + i
        if nx > 100 or visited[nx]:
            continue
        flag = False
        for f, t in road:
            if nx == f:
                q.append((t, cnt+1))
                visited[t] = True
                flag = True
        if flag:
            continue
        q.append((nx, cnt+1))
        visited[nx] = True


# 3 7
# 32 62
# 42 68
# 12 98
# 95 13
# 97 25
# 93 37
# 79 27
# 75 19
# 49 47
# 67 17