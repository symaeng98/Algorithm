import sys

sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().strip().split())
parents = [i for i in range(n+1)]

def get_parent(x):
    if parents[x] == x:
        return x
    parents[x] = get_parent(parents[x])
    return parents[x]


def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for _ in range(m):
    command, a, b = map(int, input().split())
    if command == 0:
        union_parent(a, b)
    elif command == 1:
        ap = get_parent(a)
        bp = get_parent(b)
        if ap == bp:
            print("yes")
        else:
            print("no")


# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1