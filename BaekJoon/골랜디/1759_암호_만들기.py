# from itertools import combinations
#
# l, c = map(int, input().split())
# arr = list(input().split())
#
# arr.sort()
# for comb in combinations(arr, l):
#     m, j = 0, 0
#     for c in comb:
#         if c in ['a', 'e', 'i', 'o', 'u']:
#             m += 1
#         else:
#             j += 1
#     if m >= 1 and j >= 2:
#         print(''.join(comb))


l, c = map(int, input().split())
arr = list(input().split())
arr.sort()

def process(indexes):
    if len(indexes) == l:
        now = ""
        for i in indexes:
            now += arr[i]

        m, j = 0, 0
        for x in now:
            if x in ['a', 'e', 'i', 'o', 'u']:
                m += 1
            else:
                j += 1
        if m >= 1 and j >= 2:
            print(''.join(now))
        return

    for i in range(c):
        if indexes and i <= indexes[-1]:
            continue
        indexes.append(i)
        process(indexes)
        indexes.pop()

process([])