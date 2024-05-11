a, p = map(int, input().split())
d = [a]

now = 0
while True:
    x = str(d[now])
    sum_value = 0
    for k in x:
        sum_value += int(k)**p

    if sum_value in d:
        print(d.index(sum_value))
        break

    d.append(sum_value)
    now += 1