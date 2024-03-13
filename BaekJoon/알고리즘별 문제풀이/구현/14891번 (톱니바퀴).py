from collections import deque

def left_rotate(gear):
    gear.append(gear.popleft())

def right_rotate(gear):
    gear.appendleft(gear.pop())

def get_rotate_tf(gears):
    result = []
    for i in range(3):
        if gears[i][2] == gears[i+1][6]:
            result.append(False)
        else:
            result.append(True)
    return result

def rotate(gears, n, direction):
    rtf = get_rotate_tf(gears)
    if direction == -1:
        left_rotate(gears[n])
    else:
        right_rotate(gears[n])

    dir = direction
    for i in range(n-1, -1, -1):
        if not rtf[i]:
            break
        if dir == -1:
            right_rotate(gears[i])
        else:
            left_rotate(gears[i])
        dir = -dir

    dir = direction
    for i in range(n, 3):
        if not rtf[i]:
            break
        if dir == -1:
            right_rotate(gears[i+1])
        else:
            left_rotate(gears[i+1])
        dir = -dir

gears = [deque(map(int, input())) for _ in range(4)]
k = int(input())

for _ in range(k):
    a, b = map(int, input().split())
    rotate(gears, a-1, b)

result = 0
for i in range(4):
    if gears[i][0] == 1:
        result += 2**i

print(result)