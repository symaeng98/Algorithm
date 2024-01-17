from itertools import combinations

n = int(input())
dice = list(map(int, input().split()))
if n == 1:
    print(sum(dice)-max(dice))
else:
    three = [(0, 3, 4), (0, 1, 3), (0, 2, 4), (0, 1, 2), (3, 4, 5), (1, 3, 5), (2, 4, 5), (1, 2, 5)]
    min_one = min(dice)

    min_three = 200
    for a, b, c in three:
        min_three = min(min_three, dice[a]+dice[b]+dice[c])

    min_two = 200
    for comb in combinations([0,1,2,3,4,5], 2):
        if comb[0] + comb[1] == 5:
            continue
        min_two = min(min_two, dice[comb[0]]+dice[comb[1]])


    print(4*min_three + (8*n-12)*min_two + (n-2)*(5*n-6)*min_one)