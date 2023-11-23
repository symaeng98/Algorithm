n = int(input())

max_five = n // 5
flag = True
for i in range(max_five, -1, -1):
    x = n - (i*5)
    if x%3 != 0:
        continue
    else:
        print(i+x//3)
        flag = False
        break

if flag:
    print(-1)