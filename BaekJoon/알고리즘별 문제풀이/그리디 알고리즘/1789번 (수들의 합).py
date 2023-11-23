s = int(input())

k = 1
while True:
    sum_value = (k * (k+1))//2
    if sum_value > s:
        print(k-1)
        break
    k += 1