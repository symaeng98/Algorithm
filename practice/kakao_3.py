from itertools import combinations, product

dice = [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]

length = len(dice)
dice_index = [i for i in range(length)]

comb = list(combinations(dice_index, length//2))

max_value = -1
max_dices = [-1]*(length//2)

for c in comb:
    total_count_a = [0]*(100*(length//2)+1) # 최대 나올 수 있는 합 개수
    total_count_b = [0]*(100*(length//2)+1) # 최대 나올 수 있는 합 개수
    a_dices = []
    b_dices = []
    b_index = list(set(dice_index) - set(c))
    for i in c:
        a_dices.append(dice[i])
    for b in b_index:
        b_dices.append(dice[b])

    repeat_arr = [i for i in range(6)]
    for p in product(repeat_arr, repeat=len(a_dices)):
        sum_value = 0
        for j in range(len(p)):
            sum_value += a_dices[j][p[j]]
        total_count_a[sum_value] += 1

    repeat_arr2 = [i for i in range(6)]
    for p in product(repeat_arr, repeat=len(b_dices)):
        sum_value = 0
        for j in range(len(p)):
            sum_value += b_dices[j][p[j]]
        total_count_b[sum_value] += 1

    for i in range(1, len(total_count_b)):
        total_count_b[i] += total_count_b[i-1]

    total_sum_value = 0
    for i in range(1, len(total_count_a)):
        total_sum_value += total_count_a[i]*total_count_b[i-1]

    print(total_sum_value)
    if max_value < total_sum_value:
        max_value = total_sum_value
        for i in range(len(c)):
            max_dices[i] = c[i]+1

print(max_dices)