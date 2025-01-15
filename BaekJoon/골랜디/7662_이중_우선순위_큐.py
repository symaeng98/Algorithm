from collections import defaultdict
import heapq

t = int(input())
for _ in range(t):
    k = int(input())
    min_hp = []
    max_hp = []
    count_map = defaultdict(int)
    for _ in range(k):
        s, b = input().split()
        n = int(b)
        if s == "I":
            count_map[n] += 1
            heapq.heappush(min_hp, n)
            heapq.heappush(max_hp, -n)
        elif s == "D":
            if n == 1:
                while max_hp:
                    x = heapq.heappop(max_hp)
                    if count_map[-x] == 0:
                        continue
                    count_map[-x] -= 1
                    break
            elif n == -1:
                while min_hp:
                    x = heapq.heappop(min_hp)
                    if count_map[x] == 0:
                        continue
                    count_map[x] -= 1
                    break
            else:
                print("명령어 오류")
        else:
            print("명령어 오류")
        # print(min_hp, max_hp)
        # print(count_map)

    min_num = None
    while min_hp:
        x = heapq.heappop(min_hp)
        if count_map[x] == 0:
            continue
        count_map[x] -= 1
        min_num = x
        break

    max_num = None
    while max_hp:
        x = heapq.heappop(max_hp)
        if count_map[-x] == 0:
            continue
        count_map[-x] -= 1
        max_num = -x
        break

    if min_num and (max_num is None):
        print(min_num, min_num)
    elif (min_num is None) and (max_num is None):
        print("EMPTY")
    else:
        print(max_num, min_num)




# 2
# 7
# I 16
# I -5643
# D -1
# D 1
# D 1
# I 123
# D -1
# 9
# I -45
# I 653
# D 1
# I -642
# I 45
# I 97
# D 1
# D -1
# I 333