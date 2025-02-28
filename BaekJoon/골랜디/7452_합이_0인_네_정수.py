import sys

input = sys.stdin.readline
a, b, c, d = [], [], [], []
for i in range(int(input())):
    a1, b1, c1, d1 = map(int, input().rstrip().split())
    a.append(a1)
    b.append(b1)
    c.append(c1)
    d.append(d1)


def sum(a, b, c, d):
    result = 0
    result_map = dict()
    for ax in a:
        for bx in b:
            tmp = ax + bx
            result_map[tmp] = result_map.get(tmp, 0) + 1

    for cx in c:
        for dx in d:
            tmp = cx + dx
            result += result_map.get(-tmp, 0)

    return result


print(sum(a, b, c, d))
