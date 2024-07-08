from itertools import permutations
x = int(input())
arr = list(str(x))

tmp = []
for p in permutations(arr):
    tmp.append(''.join(p))

tmp.sort()
for t in tmp:
    if int(t) > x:
        print(t)
        break