from itertools import combinations

n = int(input())
s = input()

tmp = [i for i in range(n-1)]

str_arr = []

for c in combinations(tmp, 2):
    str_arr.append(s[0:c[0]+1])
    str_arr.append(s[c[0]+1:c[1]+1])
    str_arr.append(s[c[1]+1:])
sorted_arr = sorted(list(set(str_arr)))

result = 0
for c in combinations(tmp, 2):
    first = s[0:c[0]+1]
    second = s[c[0]+1:c[1]+1]
    third = s[c[1]+1:]
    sum_value = sorted_arr.index(first) + sorted_arr.index(second) + sorted_arr.index(third) + 3
    result = max(result, sum_value)

print(result)