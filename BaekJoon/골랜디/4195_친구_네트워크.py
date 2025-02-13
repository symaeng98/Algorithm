import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b, f_num):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        f_num[a] += f_num[b]
        f_num[b] = 0
        parent[b] = a
    elif a > b:
        f_num[b] += f_num[a]
        f_num[a] = 0
        parent[a] = b
    else:
        return

t = int(input())
for _ in range(t):
    f = int(input())
    name_map = {}
    cnt = 1
    parent = [i for i in range(200002)]
    f_num = [0]*200002
    for _ in range(f):
        f1, f2 = input().split()
        if not name_map.get(f1):
            name_map[f1] = cnt
            f_num[cnt] = 1
            cnt += 1
        if not name_map.get(f2):
            name_map[f2] = cnt
            f_num[cnt] = 1
            cnt += 1

        v1, v2 = name_map[f1], name_map[f2]

        union(parent, v1, v2, f_num)
        p = find_parent(parent, v1)
        # print(f_num[1:cnt])
        # print(parent[1:cnt])
        print(f_num[p])
        

# 2
# 3
# Fred Barney
# Barney Betty
# Betty Wilma
# 3
# Fred Barney
# Betty Wilma
# Barney Betty