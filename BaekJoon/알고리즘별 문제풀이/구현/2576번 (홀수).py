odd_cnt = 0
odd_sum = 0
min_odd = 1e9
for _ in range(7):
    x = int(input())
    if x % 2 != 0:
        odd_cnt += 1
        odd_sum += x
        min_odd = min(min_odd, x)

if odd_cnt == 0:
    print(-1)
else:
    print(odd_sum)
    print(min_odd)