from itertools import combinations
arr = [int(input()) for _ in range(9)]

for c in combinations(arr, 7):
    if sum(c) == 100:
        for n in sorted(list(c)):
            print(n)
        break