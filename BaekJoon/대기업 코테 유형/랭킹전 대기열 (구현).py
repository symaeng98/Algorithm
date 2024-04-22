p, m = map(int, input().split())
room = [[] for _ in range(300)]
level_limit = [0]*300
room_member_limit = [0]*300
room_cnt = 0

for i in range(p):
    a, b = input().split()
    level, name = int(a), b

    match = False
    for j in range(room_cnt):
        if level_limit[j]-10 <= level <= level_limit[j]+10 and room_member_limit[j] < m:
            room[j].append((level, name))
            room_member_limit[j] += 1
            match = True
            break

    if not match:
        room[room_cnt].append((level, name))
        level_limit[room_cnt] = level
        room_member_limit[room_cnt] += 1
        room_cnt += 1

for r in room[:room_cnt]:
    if len(r) == m:
        print("Started!")
    else:
        print("Waiting!")
    r.sort(key=lambda x:x[1])
    for level, name in r:
        print(level, name)