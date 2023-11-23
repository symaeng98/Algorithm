a, b = input().split()

cnt = 1
while True:
    if a == b:
        print(cnt)
        break
    if int(a) > int(b):
        print(-1)
        break
    if b[-1] == '1':
        b = b[:-1]
        cnt += 1
        continue
    if int(b) % 2 == 0:
        b = str(int(b)//2)
        cnt += 1
        continue
    print(-1)
    break
