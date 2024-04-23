from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))

robots = deque([False]*n)
cnt = 1
while True:
    belt.appendleft(belt.pop())
    robots.appendleft(robots.pop())
    robots[n-1] = False

    for i in range(n-1, 0, -1):
        if robots[i-1] and belt[i] >= 1 and not robots[i]:
            belt[i] -= 1
            robots[i-1] = False
            robots[i] = True
    robots[n-1] = False

    if belt[0] > 0:
        robots[0] = True
        belt[0] -= 1

    if belt.count(0) >= k:
        break
    cnt += 1

print(cnt)