from collections import deque

wheel = [deque(map(int, input())) for _ in range(4)]
# print("first:", wheel)
def get_changed_direction(direction):
    if direction == -1:
        return 1
    else:
        return -1

def get_rotate_wheels(wn, direction):
    index = wn-1
    dir_map = {index: direction}
    # print("asdf", dir_map)
    result = []
    for i in range(index, 3):
        if wheel[i][2] == wheel[i+1][6]:
            break
        dir_map[i+1] = get_changed_direction(dir_map[i])
    for i in range(index, 0, -1):
        if wheel[i][6] == wheel[i-1][2]:
            break
        dir_map[i-1] = get_changed_direction(dir_map[i])
    for i, dc in dir_map.items():
        result.append((i, dc))
    # print(result)
    return result


k = int(input())
for _ in range(k):
    w_num, direction = map(int, input().split())
    for w, dc in get_rotate_wheels(w_num, direction):
        if dc == 1:
            wheel[w].appendleft(wheel[w].pop())
        else:
            wheel[w].append(wheel[w].popleft())
    # print(wheel)

result = 0
for i in range(4):
    if wheel[i][0] == 1:
        result += 2**i

print(result)

# 10101111
# 01111101
# 11001110
# 00000010
# 2
# 3 -1
# 1 1