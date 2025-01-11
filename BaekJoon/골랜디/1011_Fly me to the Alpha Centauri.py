t = int(input())
for _ in range(t):
    x, y = map(int, input().split())

    distance = y-x
    cnt = 0
    move = 1
    move_plus = 0
    while True:
        if move_plus >= distance:
            break
        cnt += 1
        move_plus += move
        if cnt % 2 == 0:
            move += 1

    print(cnt)


# 3
# 0 3
# 1 5
# 45 50